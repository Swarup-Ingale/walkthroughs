# URL
https://training.olicyber.it/challenges#challenge-289

# Concept
This challenge tests the ability to use `pwntools` to interact with a remote binary, specifically leveraging the `ELF()` class to parse symbol information from a binary. The core concepts are:

1. **pwntools ELF class**: `ELF()` loads an ELF binary and provides access to its symbols, sections, and data. `exe.sym` returns a dictionary mapping symbol names to their virtual addresses.

2. **pwntools remote/process**: `remote()` connects to a remote server, while `process()` runs a local binary — both return a tube object with the same API (`recv`, `send`, `recvuntil`, etc.).

3. **Binary analysis**: The challenge binary contains a hardcoded mapping of function names to their addresses. The program randomly picks from 6 function names and asks the player to supply the correct address.

### How the Binary Works

Disassembling `main` reveals:

```
names array (0x4040a0): ["dead", "beef", "c0de", "foo", "cafe", "bebe"]
addresses array (0x403de0): [0x4011c2, 0x4011d5, 0x4011e8, 0x4011fb, 0x40120e, 0x401221]
```

The flow is:
1. Print welcome banner and instructions
2. Wait for a keypress via `getchar()`
3. Set `alarm(10)` — 10 second timeout
4. Seed `srand(time(0))`
5. Loop 20 times:
   - `rand() % 6` picks a random index 0–5
   - `printf("-> %s: ", names[index])` asks for the address
   - `scanf("%lx", &input)` reads a hex address
   - Compare `input` with `addresses[index]`
   - If any mismatch → print `"[-] Sbagliato!"` and exit
6. If all 20 correct → print `"[+] Congratulazioni! Ecco la flag : flag{...}"`

# Method of Solve

### Step 1: Analyze the Binary

Use `pwntools` to load the binary and extract the name-to-address mapping:

```python
from pwn import *

exe = ELF("./sw-19")

# Read the names array (6 pointers to strings)
for i in range(6):
    ptr = u64(exe.read(0x4040a0 + i*8, 8))
    name = exe.read(ptr, 20)
    print(f"names[{i}] = {name.strip(b'\\x00').decode()}")

# Read the addresses array (6 qwords)
for i in range(6):
    addr = u64(exe.read(0x403de0 + i*8, 8))
    print(f"addresses[{i}] = {hex(addr)}")
```

This reveals the mapping:

| Name   | Address   |
|--------|-----------|
| `dead` | `0x4011c2` |
| `beef` | `0x4011d5` |
| `c0de` | `0x4011e8` |
| `foo`  | `0x4011fb` |
| `cafe` | `0x40120e` |
| `bebe` | `0x401221` |

### Step 2: Write the Exploit

The exploit connects to the remote server, waits for each prompt, parses the function name, and sends back the correct address:

```python
#!/usr/bin/env python3
from pwn import *

exe = ELF('./sw-19')

name_to_addr = {
    b'dead': 0x4011c2,
    b'beef': 0x4011d5,
    b'c0de': 0x4011e8,
    b'foo':  0x4011fb,
    b'cafe': 0x40120e,
    b'bebe': 0x401221,
}

if args.REMOTE:
    p = remote('software-19.challs.olicyber.it', 13002)
else:
    p = process([exe.path])

# Wait for the prompt and send any key to start
p.recvuntil(b'...')
p.sendline()

# Answer 20 random questions
for _ in range(20):
    p.recvuntil(b'-> ')
    name = p.recvuntil(b': ', drop=True)
    p.sendline(hex(name_to_addr[name]).encode())

# Receive the flag
p.recvuntil(b'flag{')
flag = b'flag{' + p.recvuntil(b'}', drop=True) + b'}'
print(flag.decode())
p.close()
```

### Step 3: Run Against Remote

```bash
$ python3 exploit.py REMOTE
flag{e353daccc34b6fbd}
```

## Alternative Approach

Since the binary is not PIE, the addresses are fixed. We could also use `exe.sym` to dynamically query function addresses instead of hardcoding them:

```python
name_to_addr = {
    name: exe.sym[name.decode()]
    for name in [b'dead', b'beef', b'c0de', b'foo', b'cafe', b'bebe']
}
```

This makes the script reusable across different binaries.

# Flag

```
flag{e353daccc34b6fbd}
```
- So the final flag is **flag{e353daccc34b6fbd}**
