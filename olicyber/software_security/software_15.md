# URL
https://training.olicyber.it/challenges#challenge-285

# Concept
The `break` command sets breakpoints either at function names or specific addresses (e.g., `break *main+88`). `disassemble` shows function instructions with offsets, helping locate the right breakpoint. Once stopped, `x/gx` examines memory as 8-byte hex at the target address (`$rbp-0x8`).

# Method of Solve
1. **Disassemble main** to find the `puts` call:
   ```
   disassemble main
   ```
2. **Set breakpoint** at the puts call instruction:
   ```
   break *main+88
   ```
3. **Run** the program — hits the breakpoint before `puts`.
4. **Examine the variable** at `$rbp-0x8` as hex:
   ```
   x/gx $rbp-0x8
   ```
   Output: `0x0000002823a0c041`
5. **Strip leading zeros and `0x`**: `2823a0c041`

# Flag
`flag{2823a0c041}`
- So the final flag is **flag{2823a0c041}**
