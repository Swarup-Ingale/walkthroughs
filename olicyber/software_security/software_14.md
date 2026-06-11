# URL
https://training.olicyber.it/challenges#challenge-284

# Concept
The `x` (examine) command in gdb reads memory at a given address. The format `/f` interprets the bytes as a floating-point value. Combining an address expression like `$rbp-4` lets us read a local variable on the stack.

# Method of Solve
1. **Run the binary in gdb**:
   ```
   gdb ./sw-14
   ```
2. **Execute with `run`** — the program hits `int 3` and stops.
3. **Examine `$rbp-4` as float**:
   ```
   x/f $rbp-4
   ```
   Output: `0x7fffffffdb4c:	31337.1328`
4. **Take only the integer part**: `31337`

# Flag
`flag{31337}`
- So the final flag is **flag{31337}**
