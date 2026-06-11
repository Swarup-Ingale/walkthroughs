# URL
https://training.olicyber.it/challenges#challenge-262

## Concept
Dynamic analysis is the process of analyzing a program by executing it and observing its behavior at runtime, as opposed to static analysis which examines the code without running it. Tools like `ltrace` intercept and log library calls made by a running program.

`ltrace` specifically intercepts dynamic library calls. In this challenge, the binary calls `open()` on the flag file, and `ltrace` reveals the filename (which contains the flag) before the actual file operation.

## Method of Solve
1. **Identify the binary**: The target is a 64-bit ELF executable located at `sw-08`.
2. **Make executable**: `chmod +x sw-08`
3. **Run with ltrace**: `ltrace ./sw-08`
4. **Observe output**: `ltrace` intercepts the `open()` call and shows its first argument — the filename string:

```
open("flag{e25b8bdf}", 0, ...)
```

The flag is contained directly in the filename passed to `open()`.

## Flag
`flag{e25b8bdf}`
- So the final flag is **flag{e25b8bdf}**
