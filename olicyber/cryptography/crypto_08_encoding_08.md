# URL
https://training.olicyber.it/challenges#challenge-332

# Concept 
To Understand how we can provide proper padding and how encryption and decryption work in different algorithms such as **AES | DES | CHACHA20**

# Method of Solve
- Go to the challenge URL and read the description thoroughly
- Connect to the challenge server using the provided nc command
  ```
    nc crypto-07.challs.olicyber.it 30000
  ```
- Solve the challenge by writing codes using the  Crypto.Cipher and Crypto.Util.Padding packages of python and solve the challenge to get the flag
- Ive created a universal solver for AES, DES and CHACHA20 and will be providing it soon on my github so make sure to check that out.
- First the challenge says to encrypt the provided plaintext using DES CBC mode :
  ```
    Buondì! Benvenuto al primo tutorial su PyCryptodome.
    Per ottenere la flag, rispondi correttamente ai quesiti facendo uso degli algoritmi simmetrici offerti dalla libreria.
    
    Cipher = DES
    Mode of operation = CBC
    key.hex() = 'e1976166d52f4684'
    plaintext = 'La lunghezza di questa frase non è divisibile per 8'
    Padding scheme = x923
  ```
- Once we solve this it moves on to the next part and asks us to encrypt the Plaintext again using the AES256 CFB mode:
  ```
    Cipher = AES256
    Mode of operation = CFB
    plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
    Padding scheme = pkcs7 (block size = 16)
    Segment size = 24
  ```
- And finally it asks us to decrypt the the CHACHA20 encrypted ciphertext into plaintext:
  ```
    Cipher = ChaCha20
    key.hex() = '51b4369b116fb8b71d68b12067fe3de8d11dfc36907ef3f881884b95e0f23d42'
    ciphertext.hex() = 'fabbb21850794bfa6c52a6cf72856f8f6d2eebf4b12530c4d15a9368'
    Nonce = cipher.nonce.hex() = '90d40e8e9d33f3fa'
  ```
- Finally after solving it successfully we get the flag.
- The FLag is **flag{4rt1ficial_Symm3trY_Yrt3mmyS_laicif1tr4}**
