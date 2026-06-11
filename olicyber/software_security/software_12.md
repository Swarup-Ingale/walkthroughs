# URL
https://training.olicyber.it/challenges#challenge-282

# Concept
`int 3` is a software interrupt used by debuggers for breakpoints. When a program hits an `int 3` instruction, it raises `SIGTRAP` and stops. Using `gdb`, we can run the program, let it stop at the `int 3`, and inspect the CPU registers with `info registers`.

# Method of Solve
1. **Run the binary in gdb**:
   ```
   gdb ./sw-12
   ```
2. **Execute with `run`** — the program hits `int 3` and raises `SIGTRAP`.
3. **Read registers** with `info registers rax rbx rcx`:
   ```
   rax            0x15af56
   rbx            0xf2f429
   rcx            0x5e9d38
   ```
4. **Concatenate** the hex values (without `0x` prefix):
   `15af56` + `f2f429` + `5e9d38` = `15af56f2f4295e9d38`

# Flag
`flag{15af56f2f4295e9d38}`
- So the final flag is **flag{15af56f2f4295e9d38}**
