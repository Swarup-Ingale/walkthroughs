# URL
https://training.olicyber.it/challenges#challenge-260

---

## Concept

The flag is not stored as plaintext in the binary. Instead, it is stored as an **XOR-encrypted** value. The program:

1. Reads user input (max 256 bytes)
2. Checks if the input length is exactly **14** characters
3. XORs each byte of the input with a **key** (also stored in the binary)
4. Compares the result against a stored **ciphertext** (labeled `flag`)
5. If they match, prints the success message

```c
for (local_120 = 0; local_120 < 0xe; local_120 = local_120 + 1) {
    local_118[local_120] = local_118[local_120] ^ key[local_120];
}
iVar1 = memcmp(local_118, flag, 0xe);
```

Since XOR is symmetric (A XOR B = C implies A = C XOR B), we can recover the correct input by XORing the stored ciphertext with the key.

---

## Method of Solution

### 1. Analyze the Binary with Ghidra

Import the binary into Ghidra and examine the `main` function. The decompiled code reveals:

- **`flag`** at address `0x00102008` (14 bytes of ciphertext)
- **`key`** at address `0x00102018` (14 bytes of XOR key)
- The check: `memcmp(input_xor_key, flag, 14)` must return 0

### 2. Extract the Data

Using Ghidra's "Read Bytes" functionality or any hex viewer:

```
flag (14 bytes):  d4 5c dc bb 6b 1e d3 4a 4a 5e d2 df ac 7c
key  (14 bytes):  b2 30 bd dc 10 7a e1 7b 2c 3b e2 ec 99 01
```

### 3. XOR to Recover the Flag

Since `input XOR key = ciphertext`, the correct input is `ciphertext XOR key`:

```python
flag = bytes.fromhex('d45cdcbb6b1ed34a4a5ed2dfac7c')
key  = bytes.fromhex('b230bddc107ae17b2c3be2ec9901')
input_bytes = bytes([f ^ k for f, k in zip(flag, key)])
print(input_bytes.decode())  # flag{d21fe035}
```

| Byte | Ciphertext | Key  | XOR Result | ASCII |
|------|-----------|------|------------|-------|
| 0    | 0xd4      | 0xb2 | 0x66       | `f`   |
| 1    | 0x5c      | 0x30 | 0x6c       | `l`   |
| 2    | 0xdc      | 0xbd | 0x61       | `a`   |
| 3    | 0xbb      | 0xdc | 0x67       | `g`   |
| 4    | 0x6b      | 0x10 | 0x7b       | `{`   |
| 5    | 0x1e      | 0x7a | 0x64       | `d`   |
| 6    | 0xd3      | 0xe1 | 0x32       | `2`   |
| 7    | 0x4a      | 0x7b | 0x31       | `1`   |
| 8    | 0x4a      | 0x2c | 0x66       | `f`   |
| 9    | 0x5e      | 0x3b | 0x65       | `e`   |
| 10   | 0xd2      | 0xe2 | 0x30       | `0`   |
| 11   | 0xdf      | 0xec | 0x33       | `3`   |
| 12   | 0xac      | 0x99 | 0x35       | `5`   |
| 13   | 0x7c      | 0x01 | 0x7d       | `}`   |

---

## Flag

```
flag{d21fe035}
```

- so the flag is **flag{d21fe035}**
