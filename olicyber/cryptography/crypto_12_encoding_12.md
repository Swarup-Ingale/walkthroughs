# URL
https://training.olicyber.it/challenges#challenge-337

# Concept
Interactive Diffie-Hellman tutorial covering: Euler's totient for primes, discrete logarithm, and full DH key exchange.

# Method of Solve
- Connect: `nc crypto-12.challs.olicyber.it 30005`
- Three question types:
  1. **Euler's totient for a prime p**: all numbers 1..p-1 are coprime → answer: `p-1`
  2. **Discrete logarithm**: find `k` such that `base^k ≡ x (mod p)` — brute force for small moduli, integer power check for powers of 2
  3. **DH Key Exchange**: given `p, g` and server's public key, send our public key `g^b mod p`, then compute shared secret `server_pub^b mod p`

# Final Script
```python
import socket, re, time, random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(15)
s.connect(('crypto-12.challs.olicyber.it', 30005))

def recv_until(seq, timeout=10):
    buf = b""
    s.settimeout(timeout)
    while True:
        try:
            c = s.recv(1)
            if not c: break
            buf += c
            if seq in buf: break
        except socket.timeout: break
    s.settimeout(15)
    return buf.decode()

def send(t):
    s.sendall((str(t) + '\n').encode())
    time.sleep(0.3)

def dlog(base, x, mod):
    for k in range(1, 100000):
        if pow(base, k, mod) == x:
            return k
    return None

data = recv_until(b'? ')
print(data, end='')

b = p = g = server_pub = None

while True:
    if 'flag{' in data:
        m = re.search(r'flag\{[^}]+\}', data)
        print(f"\nFLAG: {m.group()}"); break

    if 'quanti numeri positivi minori di p' in data:
        print("  -> p-1"); send('p-1')

    elif 'logaritmo discreto' in data:
        m = re.search(r'(\d+) in base (\d+).*?(\d+)', data)
        if m:
            x, base, mod = int(m.group(1)), int(m.group(2)), int(m.group(3))
            ans = dlog(base, x, mod)
            print(f"  -> log_{base}({x}) mod {mod} = {ans}"); send(ans)
        else:
            send("0")

    elif 'pubblica' in data:
        m = re.search(r'p = (\d+), g = (\d+)', data)
        if m: p, g = int(m.group(1)), int(m.group(2))
        m2 = re.search(r'chiave pubblica [eè] (\d+)', data)
        if m2: server_pub = int(m2.group(1))
        b = random.randint(2, p-2)
        pub = pow(g, b, p)
        print(f"  -> Public key: {pub}"); send(pub)

    elif 'condivisa' in data:
        shared = pow(server_pub, b, p)
        print(f"  -> Shared secret: {shared}"); send(shared)

    else:
        send("0")

    data = recv_until(b'? ', timeout=5)
    if data: print(data, end='')
    else: break

s.close()
```
- After running the automated script we get the flag.
- The flag is **flag{W3_st4Nd_t0d4Y_0n_th3_Br1nk_of_4_r3v01uTioN_1n_Cryptography.}**
