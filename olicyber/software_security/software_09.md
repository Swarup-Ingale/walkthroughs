# URL
https://training.olicyber.it/challenges#challenge-263

# Concept
`strace` intercepts and logs **system calls** (syscalls) made by a process, unlike `ltrace` which intercepts **library calls**. This distinction matters when the binary is **statically linked** — `ltrace` cannot instrument static binaries because there are no dynamic library calls to hook. `strace` works at the kernel interface level, tracing syscalls like `open()`, `openat()`, `read()`, `write()`, etc., regardless of whether the binary is statically or dynamically linked.

# Method of Solve
- **Identify the binary**: A statically linked 64-bit ELF executable at `sw-09` (much larger file size confirms static linking).
- **Make executable**: `chmod +x sw-09`
- **Run with strace**: `strace ./sw-09`
- **Observe output**: `strace` intercepts the `openat()` syscall and reveals the filename argument:

```
openat(AT_FDCWD, "flag{01b81d48}", O_RDONLY) = -1 ENOENT
```

The flag is embedded in the filename string passed to `openat()`.

## Flag
`flag{01b81d48}`
- So the final flag is **flag{01b81d48}**
