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
