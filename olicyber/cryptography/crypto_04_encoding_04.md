# URL
https://training.olicyber.it/challenges#challenge-329

# Concept
To Understand How XOR works and how we can use it for encoding and decoding in Cryptography.

# Method of Solve
- Go to the Challenge URL and copy the two messages m1 and m2
- Write a Python Script for performing XOR of both bit wise ... to get the flag
  ```
    # Given hex strings
    m1_hex = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
    m2_hex = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"
    
    # Convert hex strings to bytes
    m1 = bytes.fromhex(m1_hex)
    m2 = bytes.fromhex(m2_hex)
    
    # XOR byte-by-byte (up to the shortest length)
    xor_bytes = bytes(b1 ^ b2 for b1, b2 in zip(m1, m2))
    
    # Print raw bytes
    print("XOR result (bytes):", xor_bytes)
    
    # Try to decode as ASCII (replace errors if non-printable)
    decoded = xor_bytes.decode("ascii", errors="replace")
    print("XOR result (ASCII):", decoded)
  ```
- First we convert the hexx into bytes to perform XOR of every Byte
- Now we will Perform XOR of both the messages
- The flag is **flag{x0R_f0r_th3_w1n!}**
