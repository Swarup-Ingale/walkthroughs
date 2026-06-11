# URL
https://training.olicyber.it/challenges#challenge-283

# Concept
The `print` (or `p`) command in gdb evaluates expressions and prints their values. With the `/d` format specifier, it prints as a signed decimal integer. This allows reading the value of a register like `$rax` at a breakpoint.

# Method of Solve
1. **Run the binary in gdb**:
   ```
   gdb ./sw-13
   ```
2. **Execute with `run`** — the program hits `int 3` and stops.
3. **Print `$rax` as signed decimal**:
   ```
   print/d $rax
   ```
   Output: `$1 = -415710747049308268`
4. **Remove the minus sign** and wrap in flag{}.

# Flag
`flag{415710747049308268}`
- So the final flag is **flag{415710747049308268}**
