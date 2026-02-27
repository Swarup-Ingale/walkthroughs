# 🎮 Gameshell — HackMyVM Writeup
## Introduction

This writeup documents the complete exploitation process of the Gameshell machine from HackMyVM.
The goal of this machine is to perform a full attack chain starting from initial network discovery to privilege escalation and root compromise.

This machine focuses on:

- Network enumeration
- Web application exploitation (Ruby-based)
- Server-Side Template Injection (SSTI)
- Local service pivoting
- FastCGI exploitation
- Privilege escalation via sudo misconfiguration

The objective is to gain:
- User flag
- Root flag

All attacks were performed from a Kali Linux attacker machine inside a VirtualBox lab environment.

## Lab Setup

| Machine    | Role     | Network           |
| ---------- | -------- | ----------------- |
| Kali Linux | Attacker | 192.168.56.0/24   |
| Gameshell  | Target   | Host-Only Network |

Both machines were configured using Host-Only Adapter in VirtualBox to allow direct communication.

---

## Step 1 — Target Discovery

Since this machine was imported locally in VirtualBox, the first step was to discover its IP address on the internal lab network.

I performed a network sweep using arp-scan.

### Command Used
  ```bash
    sudo arp-scan --interface=eth1 192.168.56.0/24
  ```
arp-scan sends ARP requests to all hosts in the specified subnet. ARP works at Layer 2 (Data Link Layer) and detects live hosts even if ICMP (ping) is disabled. It is faster and more reliable in local lab environments.

### Result
The following live host was identified:

  ```bash
    192.168.56.156
  ```
This was assumed to be the Gameshell machine.

---

## Step 2 — Host Verification

To confirm that the machine was reachable, I tested connectivity using ICMP ping.

### Command Used
  ```bash
    ping 192.168.56.156
  ```

This Command Confirms that the host is online and verifies network connectivity and also ensures correct adapter configuration. It also Confirms no firewall blocking ICMP.

### Result

The machine responded successfully to ICMP requests, confirming that:
- The target is alive.
- The network configuration is correct.
- The machine is ready for enumeration.

---

## Step 3 — Full Port Scan & Service Enumeration

After confirming that the target was alive, the next step was to enumerate all open TCP ports and identify running services.

### Command Used
  ```bash
    nmap -sC -sV -p- 192.168.56.156
  ```
The command flags represents: 
- -sC → Runs default Nmap scripts (basic enumeration & detection)
- -sV → Performs version detection
- -p- → Scans all 65535 TCP ports

### Scan Results
  ```bash
    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 8.4p1 Debian
    80/tcp   open  http    Apache httpd 2.4.62 (Debian)
    7681/tcp open  http    ttyd 1.7.7
  ```

### Analysis of Findings
**Port 22 — SSH**
- OpenSSH 8.4p1
- Likely requires credentials
- Not vulnerable by default
- Will revisit later if credentials are found

**Port 80 — Apache Web Server**
- Apache 2.4.62 (Debian)
- Website title:
  ```bash
    Bash // The Eternal Shell
  ```
This is likely the main attack surface.

**Port 7681 — ttyd Web Terminal**
- This is extremely interesting.
- ttyd is a web-based terminal emulator
- It allows shell access through a browser
- Version: 1.7.7
- The HTTP title:
  ```bash
    ttyd - Terminal
  ```
  
### Attack Surface Summary
| Port | Service             | Priority             |
| ---- | ------------------- | -------------------- |
| 22   | SSH                 | Medium (needs creds) |
| 80   | Apache Web          | High                 |
| 7681 | Web Terminal (ttyd) | VERY HIGH            |

The presence of ttyd indicates that this machine likely revolves around shell access and potential breakout techniques.

---

## Step 4 — Web Enumeration

After identifying open ports, I manually visited the exposed web services.

### Port 7681 : ttyd web terminal

When visiting:
  ```bash
    http://192.168.56.156:7681/
  ```

The page displayed an interactive terminal-style interface titled:

**Welcome to GameShell!**

The interface contained instructions such as:
  ```bash
    Run the command:
    $ gsh goal
    
    $ gsh check
    $ gsh help
  ```
It appeared to be a gamified shell environment designed to teach command-line usage.

Then the promp showed :
  ```bash
    [mission 1] $
  ```

This strongly indicates:
- The machine is intentionally exposing a shell interface
- The challenge likely revolves around shell interaction
- This may be a restricted environment

---

## Step 5 — Initial Shell Enumeration (ttyd)

After accessing the ttyd web terminal on port 7681, I began enumerating the environment.

### Checking Current User
  ```bash
    whoami
  ```
- Output:
  ```bash
    www-data
  ```
  
### Checking User Privileges
  ```bash
    id
  ```
- Output:
  ```bash
    uid=33(www-data) gid=33(www-data) groups=33(www-data)
  ```
  
This confirms:
- The shell is running as www-data
- This is the default Apache web server user
- We currently have low-privileged access

### Checking Current Working Directory
  ```bash
    pwd
  ```
- Output:
  ```bash
    /opt/gameshell/gameshell/World
  ```

This indicates that:
- We are inside a custom application directory
- The shell environment is likely part of the GameShell application
- This may be a controlled or sandboxed environment

### Listing Files and Directories
  ```bash
    ls -la
  ```
- Output:
  ```bash
    Castle
    Forest
    Garden
    Mountain
    Stall
  ```

This confirms:
- The environment is structured like a game world
- Directories represent locations
- The challenge likely involves navigating through these directories

---

## Step 6 — Shell Capability Testing

To determine whether the shell was restricted or sandboxed, I tested environment variables and filesystem access.

### Checking Default Shell
  ```bash
    echo $SHELL
  ```
- Output:
  ```bash
    /usr/sbin/nologin
  ```
This indicates that the www-data user is not meant to have interactive login access. However, since access is provided via ttyd, this restriction does not apply.

### Checking PATH Variable
  ```bash
    echo $PATH
  ```
The Observation That I made:
- Custom GameShell script directories are present.
- Standard system binary directories (/bin, /usr/bin, etc.) are also accessible.

This suggests we are not restricted to a custom command wrapper.

### Checking Bash Availability
  ```bash
    which bash
  ```
- Output:
  ```bash
    /usr/bin/bash
  ```
This confirms that the real bash binary is accessible.

### Checking Root Filesystem Access
  ```bash
    ls /
  ```

The full Linux filesystem structure was visible.

This confirms:
- The shell is NOT jailed
- The shell is NOT chrooted
- This is a real system shell running as www-data

---

## Step 7 — Identifying Command Filtering

I attempted to check sudo privileges:
  ```bash
    sudo -l
  ```
- Result:
  ```bash
    gsh: sudo: command not found
  ```
However, during SUID enumeration:
  ```bash
    find / -perm -4000 -type f 2>/dev/null
  ```
The following binary was found:
  ```bash
    /usr/bin/sudo
  ```
This indicates:
- The sudo binary exists on the system.
- However, the gsh wrapper blocks execution of certain commands.
- This confirms we are operating inside a restricted command wrapper.

---

## Step 8 — Attempting Shell Escape

Since the environment appeared to be a restricted wrapper, I attempted to spawn a real shell.

### Attempt 1 — Spawn Bash
  ```bash
    bash
  ```
- Result:

The GameShell interface reloaded and printed the mission instructions again.

This indicates that bash execution is intercepted and redirected back into the game wrapper.

### Attempt 2 — Direct Path Execution
  ```bash
    /bin/bash
  ```
- Result:

The same GameShell banner reappeared.

This confirms that even direct binary invocation is filtered.

### Attempt 3 — Using sh
  ```bash
    sh
  ```
- The prompt changed to:
  ```bash
    [mission ] $
  ```
Then:
  ```bash
    /bin/sh
  ```
- Result:
  ```bash
    /bin/sh: 1: gsh: not found
  ```
### The Key Observation that I made:
- The error:
  ```bash
    gsh: not found
  ```
- Suggests:
  - The environment depends on the gsh program.
  - The shell session is controlled by a wrapper mechanism.
  - The wrapper may rely on environment variables or PATH manipulation.
  - Breaking the wrapper may be possible by altering environment execution behavior.

---

## Step 9 — Inspecting the GameShell Wrapper

After confirming that gsh was not directly callable, I investigated the GameShell script directory.

### Checking for gsh Binary
  ```bash
    which gsh
    type gsh
  ```
- Result:
  ```bash
    gsh: not found
  ```
This indicates that gsh is not a standalone system binary.

### Inspecting Script Directory
  ```bash
    ls -la /opt/gameshell/gameshell/scripts
  ```
The directory contained numerous executable scripts such as:
  ```bash
    _gsh_env
    _gsh_goal
    _gsh_systemconfig
    _gsh_protect
    _gsh_unprotect
    admin_mode
    mainshell.sh
    generate_rcfile
    mktemp
    rm
    copy_bin
  ```
### Key Observation that I made:

The GameShell environment is implemented entirely using shell scripts.

This means:
- Command filtering is likely done in mainshell.sh
- Environment setup is likely done in _gsh_env
- Command validation may be script-based
- If any script is misconfigured, it could allow command execution bypass

---

## Step 10 — Directory Permission Analysis

To determine whether script modification was possible, I inspected directory permissions.

### Checking Script Directory Permissions
  ```bash
    ls -ld /opt/gameshell/gameshell/scripts
  ```
- Output:
  ```bash
    drwxr-xr-x 2 www-data www-data
  ```
This indicates:
- The directory is owned by www-data
- The current user is www-data
- Owner has write permission

Therefore, Script modification inside this directory may be possible.

### Checking Parent Directory Permissions
  ```bash
    ls -ld /opt/gameshell/gameshell
  ```
- Output:
  ```bash
    d--x--x--x
  ```
This indicates:
- No read permission
- No write permission
- Only execute (traversal)

This prevents listing or modifying parent directory contents.

## Step 11 — Writable PATH Directory Discovery

To test write permissions inside the script directory, I attempted to create a file:
  ```bash
    touch /opt/gameshell/gameshell/scripts/testfile
  ```
The file was successfully created:
  ```bash
    -rw-r--r-- 1 www-data www-data testfile
  ```
This confirms:
- The current user (www-data) can write inside /opt/gameshell/gameshell/scripts
- This directory appears first in the $PATH
- Any executable placed here may override system binaries

### Critical Observation that I made:

Since the script directory appears first in $PATH, this introduces a potential PATH hijacking vulnerability.

If the GameShell wrapper internally executes system commands without absolute paths, a malicious binary placed in this directory could be executed instead.

---

## 
