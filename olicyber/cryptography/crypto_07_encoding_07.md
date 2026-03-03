# URL
https://training.olicyber.it/challenges#challenge-332

# Concept 
To Understand the basic working of Cryptographic Encryption Methodology of DES, AES and how the block cipher works

# Method of Solve
- Go to the challenge URL and read the description thoroughly
- Read the description and download the dependencies of python modules provided
- Connect to the remote server using nc with given domain and port
  ```
    ┌──(venv)─(kali㉿kali)-[~/olicyber/cryptography]
    └─$ nc crypto-07.challs.olicyber.it 30000     
    Buondì! Benvenuto al primo tutorial su PyCryptodome.
    Per ottenere la flag, rispondi correttamente ai quesiti facendo uso degli algoritmi simmetrici offerti dalla libreria.
    
    Cipher = DES
    Mode of operation = CBC
    key.hex() = '667f1a70f6dab04a'
    plaintext = 'La lunghezza di questa frase non è divisibile per 8'
    Padding scheme = x923
  ```
- This is a Basic DES encryption in which we have to find the encrypted hex vslue of plaintext using the key given and provide both encrypted hex value and IV used
- I used a python script to perform encryption and kept IV default to *0*
  ```
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import pad
    import binascii
    
    # Copy-paste these exactly as they appear in the terminal
    key_hex = '667f1a70f6dab04a'
    plaintext_str = 'La lunghezza di questa frase non è divisibile per 8'
    
    BLOCK_SIZE = 8  # DES uses 8, AES uses 16
    IV = b'\x00' * BLOCK_SIZE  # Standard default if not provided
    
    # 1. Convert hex key to bytes
    key = binascii.unhexlify(key_hex)
    
    # 2. Encode string to bytes (UTF-8 is standard for 'è')
    plaintext_bytes = plaintext_str.encode('utf-8')
    
    # 3. Apply X923 Padding
    # This adds 00 bytes and a final byte indicating the length
    padded_data = pad(plaintext_bytes, BLOCK_SIZE, style='x923')
    
    # 4. Encrypt using CBC mode
    cipher = DES.new(key, DES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(padded_data)
    
    # 5. Output result in Hex
    result_hex = binascii.hexlify(ciphertext).decode()
    iv_hex = binascii.hexlify(IV).decode()
    
    print(f"--- RESULTS ---")
    print(f"Ciphertext (Hex): {result_hex}")
    print(f"IV used (Hex):     {iv_hex}")
  ```
- This gives solution result for 1st challenge
  ```
    ┌──(venv)─(kali㉿kali)-[~/olicyber/cryptography]
    └─$ python3 07_encoding.py
    --- RESULTS ---
    Ciphertext (Hex): cda19f1411e82d5ab0041aec1d7737df9b357e562ba4817378d4a031c2c92e274b865cd25ff255667ae2703091a533ed02aa8698e9885e6f
    IV used (Hex):     0000000000000000
  ```
- When we provide this to the server it responds as follows and gives next challenge
  ```
    Qual è il testo cifrato (in esadecimale)? cda19f1411e82d5ab0041aec1d7737df9b357e562ba4817378d4a031c2c92e274b865cd25ff255667ae2703091a533ed02aa8698e9885e6f
    Che IV hai utilizzato (in esadecimale)? 0000000000000000
    Corretto!
    
    
    Cipher = AES256
    Mode of operation = CFB
    plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
    Padding scheme = pkcs7 (block size = 16)
    Segment size = 24
  ```
- Now in the Part 02 of the challenge we can see its shifted to AES256 encryption and Mode of operation as CFB
- So now we have to again use the provided plaintext and padding scheme to generate a key and then use the key to generate a ciphertext
- for this I used another python script
  ```
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import binascii
    
    # We define a 32-byte key (64 hex characters) because it's AES-256
    my_key_hex = '01' * 32 
    plaintext_str = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
    
    BLOCK_SIZE = 16 # AES is always 16
    SEGMENT_SIZE = 24 # From the prompt
    
    key = binascii.unhexlify(my_key_hex)
    plaintext_bytes = plaintext_str.encode('utf-8')
    
    # 1. Apply PKCS7 Padding
    padded_data = pad(plaintext_bytes, BLOCK_SIZE, style='pkcs7')
    
    # 2. Initialize AES-256 in CFB mode
    # Using a null IV again (16 bytes for AES)
    iv = b'\x00' * 16
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=SEGMENT_SIZE)
    
    # 3. Encrypt
    ciphertext = cipher.encrypt(padded_data)
    
    print(f"Key to send to server: {my_key_hex}")
    print(f"Resulting Ciphertext:  {binascii.hexlify(ciphertext).decode()}")
  ```
- This gives the result and when we feed it to the server we get the final part 03 of the challenge.
  ```
    ┌──(venv)─(kali㉿kali)-[~/olicyber/cryptography]
    └─$ python3 07_encoding_02.py
    Key to send to server: 0101010101010101010101010101010101010101010101010101010101010101
    Resulting Ciphertext:  3ff1ea1333c43c0c524146da060c400e75af59c90d3b0b2779e337847c942ff2be6391970543f097401d367042bb8312854e845338605b2cde491462a598096a80f8a34e51f2131a5afcafbd09f2433b
  ```
- Now we get to the final part of the challenge
  ```
    Che chiave vuoi che usi (in esadecimale)? 0101010101010101010101010101010101010101010101010101010101010101
    Corretto!
    
    Qual è il testo cifrato (in esadecimale)? 3ff1ea1333c43c0c524146da060c400e75af59c90d3b0b2779e337847c942ff2be6391970543f097401d367042bb8312854e845338605b2cde491462a598096a80f8a34e51f2131a5afcafbd09f2433b
    Che IV hai utilizzato (in esadecimale)? 00000000000000000000000000000000
    Corretto!
    
    Passiamo ora a uno stream cipher.
    
    Cipher = ChaCha20
    key.hex() = 'b73c44b7f14704d5c70e1fd58d215567b7207065b523723773c6cd803e663f99'
    ciphertext.hex() = 'd74edab6ea87450b870b06f145ee83fe5f50fc9ac31e7be6ef111aa5'
    Nonce = cipher.nonce.hex() = 'f47fa8e27faca74e'
  ```
- As we can see now we have to use ChaCha20 encryption technique which is a stream cipher technique and uses nonce we have to decrypt the given ciphertext into ASCII encoded plaintext
- I did it again using a python script as follows
  ```
    from Crypto.Cipher import ChaCha20
    import binascii
    
    key_hex = 'b73c44b7f14704d5c70e1fd58d215567b7207065b523723773c6cd803e663f99'
    ciphertext_hex = 'd74edab6ea87450b870b06f145ee83fe5f50fc9ac31e7be6ef111aa5'
    nonce_hex = 'f47fa8e27faca74e'
    
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    nonce = binascii.unhexlify(nonce_hex)
    
    # Initialize ChaCha20 with the provided key and nonce
    cipher = ChaCha20.new(key=key, nonce=nonce)
    
    # Decrypt the ciphertext
    plaintext_bytes = cipher.decrypt(ciphertext)
    
    # Convert bytes back to a readable string
    print(f"Plaintext (ASCII): {plaintext_bytes.decode('utf-8')}")
  ```
- This gives us the following results
  ```
    ┌──(venv)─(kali㉿kali)-[~/olicyber/cryptography]
    └─$ python3 07_encoding_03.py
    Plaintext (ASCII): Decrypting with mambo rhythm
  ```
- When we feed this to the server, we get the flag in response
  ```
    Qual è il testo in chiaro (ASCII)? Decrypting with mambo rhythm
    Corretto!
    
    Grande! flag{4rt1ficial_Symm3trY_Yrt3mmyS_laicif1tr4}
  ```
- The Flag is **flag{4rt1ficial_Symm3trY_Yrt3mmyS_laicif1tr4}**
