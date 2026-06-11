# URL
https://training.olicyber.it/challenges#challenge-286

# Concept
GDB's `set` command can modify memory at runtime. By setting a global variable (`tochange`) to the expected value (`0xdeadc0debadc0ffe`) while the program is paused at `sleep`, the check passes and the flag is printed.

# Method of Solve
1. **Set breakpoint on sleep**:
   ```
   break *main+81
   ```
2. **Run the program** — it stops when `sleep` is called.
3. **Find and set `tochange`** using `p &tochange` to get its address (`0x404038`), then:
   ```
   set {long}(0x404038) = 0xdeadc0debadc0ffe
   ```
4. **Continue execution** — the check passes and the flag is printed:
   ```
   flag{1980000802282532}
   ```

# Flag
`flag{1980000802282532}`
- So the final flag is **flag{1980000802282532}**
