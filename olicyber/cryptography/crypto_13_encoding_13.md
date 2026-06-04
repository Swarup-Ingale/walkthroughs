# URLhttps://training.olicyber.it/challenges#challenge-338

# Concept
Full Diffie-Hellman protocol with custom parameters: generate a 1024-bit safe prime, find a generator, exchange keys, then decrypt an AES-CBC encrypted message using the shared secret.

# Method of Solve
- Connect: `nc crypto-13.challs.olicyber.it 30006`
- Generate a **safe prime** `p` (1024 bits, where `(p-1)//2` is also prime) using `cryptography` library's DH parameters
- Find a **generator** `g` for the group: for a safe prime `p = 2q+1`, test small integers where `g² ≢ 1` and `g^q ≢ 1 (mod p)`
- Send `p` and `g` to the server
- Alice asks for our public key → send `g^b mod p` where `b` is random
- Alice responds with her public key (in hex) and an **AES-CBC encrypted message**
- Decrypt using the **first 16 bytes** of the shared secret `A^b mod p` as the AES-128 key

# Final Script
```python
import socket, re, time, random
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)
s.connect(('crypto-13.challs.olicyber.it', 30006))

def read(timeout=3):
    buf = b""
    s.settimeout(timeout)
    while True:
        try:
            d = s.recv(4096)
            if not d: break
            buf += d
        except socket.timeout: break
    s.settimeout(30)
    return buf.decode(errors='ignore')

def send(t):
    s.sendall((str(t) + '\n').encode())
    time.sleep(0.5)

def find_generator(p):
    q = (p - 1) // 2
    for g in range(2, 1000):
        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
            return g
    return None

params = dh.generate_parameters(generator=2, key_size=1024, backend=default_backend())
p = params.parameter_numbers().p
g = find_generator(p)

data = read(5); print(data, end=''); send(p)
data = read(5); print(data, end=''); send(g)
data = read(5); print(data, end='')
b = random.randint(2, p-2)
my_pub = pow(g, b, p)
send(my_pub)

data = read(5); print(data, end='')
hex_match = re.search(r'[0-9a-fA-F]{50,}', data)
iv_match = re.search(r'IV:\s*([0-9a-fA-F]+)', data)
msg_match = re.search(r'msg:\s*([0-9a-fA-F]+)', data)

if hex_match and iv_match and msg_match:
    alice_pub = int(hex_match.group(0), 16)
    shared = pow(alice_pub, b, p)
    shared_bytes = shared.to_bytes((shared.bit_length() + 7) // 8, 'big')
    key = shared_bytes[:16]  # AES-128
    iv = bytes.fromhex(iv_match.group(1))
    ct = bytes.fromhex(msg_match.group(1))

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    pt = cipher.decryptor().update(ct) + cipher.decryptor().finalize()
    unpadder = padding.PKCS7(128).unpadder()
    pt = unpadder.update(pt) + unpadder.finalize()
    print(f"\n[+] FLAG: {pt.decode()}")

s.close()
```
- The flag is **flag{D1_qU3st1_73mPi_CrYP70_3_+_1mp0R74Nte_cH3_m4i}**
