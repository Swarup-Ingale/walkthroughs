# URL 
https://training.olicyber.it/challenges#challenge-261

---

# Concept

The flag is never stored as a data string in the binary. Instead, it is constructed **at runtime** by storing individual bytes onto the stack via `mov` instructions. A decompiler may optimize this away or fail to show it clearly, so examining the raw disassembly is essential.

---

# Method of Solution

### 1. Analyze with Ghidra

Import the binary and look at `main`. The decompiled view shows only:

```c
undefined8 main(void) {
    puts(&DAT_00102004);
    return 0;
}
```

This seems too simple — the challenge description warns us to inspect the disassembly, not just the decompiler output.

### 2. Examine the Disassembly

Switch to the disassembly listing at `main` (address `0x00101145`). The raw bytes reveal a series of `mov byte` instructions that write the flag character-by-character onto the stack:

```
0010115a c6 85 f0 fe ff ff 66     mov byte [rbp-0x110], 0x66   ; 'f'
00101161 c6 85 f1 fe ff ff 6c     mov byte [rbp-0x10f], 0x6c   ; 'l'
00101168 c6 85 f2 fe ff ff 61     mov byte [rbp-0x10e], 0x61   ; 'a'
0010116f c6 85 f3 fe ff ff 67     mov byte [rbp-0x10d], 0x67   ; 'g'
00101176 c6 85 f4 fe ff ff 7b     mov byte [rbp-0x10c], 0x7b   ; '{'
0010117d c6 85 f5 fe ff ff 66     mov byte [rbp-0x10b], 0x66   ; 'f'
00101184 c6 85 f6 fe ff ff 63     mov byte [rbp-0x10a], 0x63   ; 'c'
0010118b c6 85 f7 fe ff ff 32     mov byte [rbp-0x109], 0x32   ; '2'
00101192 c6 85 f8 fe ff ff 66     mov byte [rbp-0x108], 0x66   ; 'f'
00101199 c6 85 f9 fe ff ff 34     mov byte [rbp-0x107], 0x34   ; '4'
001011a0 c6 85 fa fe ff ff 34     mov byte [rbp-0x106], 0x34   ; '4'
001011a7 c6 85 fb fe ff ff 39     mov byte [rbp-0x105], 0x39   ; '9'
001011ae c6 85 fc fe ff ff 62     mov byte [rbp-0x104], 0x62   ; 'b'
001011b5 c6 85 fd fe ff ff 7d     mov byte [rbp-0x103], 0x7d   ; '}'
001011bc c6 85 fe fe ff ff 00     mov byte [rbp-0x102], 0x00   ; null terminator
```

### 3. Extract the Flag

Reading the immediate values (the last byte of each instruction) in order:

| Offset | Hex Value | ASCII |
|--------|-----------|-------|
| 0x66   | `f`       | `f`   |
| 0x6c   | `l`       | `l`   |
| 0x61   | `a`       | `a`   |
| 0x67   | `g`       | `g`   |
| 0x7b   | `{`       | `{`   |
| 0x66   | `f`       | `f`   |
| 0x63   | `c`       | `c`   |
| 0x32   | `2`       | `2`   |
| 0x66   | `f`       | `f`   |
| 0x34   | `4`       | `4`   |
| 0x34   | `4`       | `4`   |
| 0x39   | `9`       | `9`   |
| 0x62   | `b`       | `b`   |
| 0x7d   | `}`       | `}`   |

```python
import re
# raw hex of the mov instructions region
raw = 'c685f0feffff66c685f1feffff6cc685f2feffff61c685f3feffff67c685f4feffff7bc685f5feffff66c685f6feffff63c685f7feffff32c685f8feffff66c685f9feffff34c685fafeffff34c685fbfeffff39c685fcfeffff62c685fdfeffff7dc685fefeffff00'
matches = re.findall(r'c685[0-9a-f]{2}feffff([0-9a-f]{2})', raw)
flag = ''.join(chr(int(m, 16)) for m in matches)
print(flag)  # flag{fc2f449b}
```

---

# Flag

```
flag{fc2f449b}
```
- so the final flag is **flag{fc2f449b}**
