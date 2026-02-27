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

# Lab Setup

| Machine    | Role     | Network           |
| ---------- | -------- | ----------------- |
| Kali Linux | Attacker | 192.168.56.0/24   |
| Gameshell  | Target   | Host-Only Network |

Both machines were configured using Host-Only Adapter in VirtualBox to allow direct communication.

# 
