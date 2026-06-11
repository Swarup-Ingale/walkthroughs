# URL
https://training.olicyber.it/challenges#challenge-265

# Concept
When a binary calls `fork()`, it creates a child process. By default, `strace` only traces the parent. The `-f` flag tells `strace` to follow child processes as well, tracing syscalls from all forked children.

# Method of Solve
1. **Run with strace following forks**:
   ```
   strace -f ./sw-11
   ```
2. **Observe child process syscall** in the output:
   ```
   [pid 52910] openat(AT_FDCWD, "flag{5a11b5a6}", O_RDONLY) = -1 ENOENT
   ```

## Flag
`flag{5a11b5a6}`
- So the final flag is **flag{5a11b5a6}**
