# URL
https://training.olicyber.it/challenges#challenge-331

# Concept 
The fundamental concept is that One-Time Pad (OTP) key reuse transforms a mathematically unbreakable cipher into a simple linguistics puzzle even if it is MTP based.

# Method of Solve
- Go to the challenge URL and get the output.txt
- It is an example of Many Time Pad (MTP) but since the key cab be reused, it becomes simple to crack it
- We can use the following code:
  ```
    import binascii
    
    def xor(a, b):
        """XORs two byte sequences."""
        return bytes(x ^ y for x, y in zip(a, b))
    
    # The provided ciphertexts
    hex_ciphers = [
        INPUT_YOUR_OUTPUT.txt
    ]
    
    ciphers = [binascii.unhexlify(c) for c in hex_ciphers]
    
    # Based on our analysis, we know the first message
    known_plaintext = "IL CRITTOSISTEMA CHE STO UTILIZZANDO SEMBRA INDISTRUTTIBILE"
    known_bytes = known_plaintext.encode()
    
    # Derive the keystream by XORing ciphertext[0] with its known plaintext
    # Note: This only gives us a key as long as the first message.
    keystream = xor(ciphers[0], known_bytes)
    
    print("--- Decrypted Messages ---")
    for i, c in enumerate(ciphers):
        # Decrypt as much as possible with the derived keystream
        decrypted = xor(c, keystream)
        # Convert bytes to string, using '?' for unknown characters beyond keystream length
        result = "".join(chr(b) if 32 <= b <= 126 else "?" for b in decrypted)
        print(f"Message {i+1}: {result}")
    
    print("\n--- The Flag ---")
    # The flag is in Message 3
    flag_decrypted = xor(ciphers[2], keystream).decode()
    print(flag_decrypted)
  ```
- This gives an italian output in which there is hidden flag
- The flag is **flag{M4ny_71m3_P4D_N1gH7m4r3}**
