# URL
https://training.olicyber.it/challenges#challenge-335

# Concept
Solving systems of modular congruences using the Chinese Remainder Theorem.

# Method of Solve
- Connect: `nc crypto-10.challs.olicyber.it 30003`
- The server presents a system:
  ```
  x % m1 = r1
  x % m2 = r2
  ...
  x % M = ?
  ```
- Compute the unique solution `x` modulo the product of all moduli using CRT
- The Extended Euclidean Algorithm is used to compute modular inverses for CRT combination
- CRT formula: `x = Σ(r_i * (M/m_i) * inv(M/m_i mod m_i)) mod M`

# Final Script
```python
import socket, re, time
from functools import reduce

def extended_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def crt(remainders, moduli):
    M = reduce(lambda a, b: a * b, moduli)
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        _, inv, _ = extended_gcd(Mi, m)
        x += r * Mi * inv
    return x % M, M

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('crypto-10.challs.olicyber.it', 30003))

def read_all(timeout=2):
    buf = b""
    s.settimeout(timeout)
    while True:
        try:
            data = s.recv(4096)
            if not data: break
            buf += data
        except socket.timeout: break
    s.settimeout(30)
    return buf.decode(errors='ignore')

def send(t): s.sendall((t+'\n').encode()); time.sleep(0.2)

data = read_all(3)
print(data, end='')
while True:
    if 'flag{' in data:
        m = re.search(r'flag\{[^}]+\}', data)
        print(f"\nFlag: {m.group()}"); break
    remainders, moduli = [], []
    for line in data.split('\n'):
        m = re.match(r'x % (\d+) = (\d+)', line)
        if m: moduli.append(int(m.group(1))); remainders.append(int(m.group(2)))
    m_big = re.search(r'x % (\d+) = \?', data)
    if m_big and moduli:
        x, _ = crt(remainders, moduli)
        result = x % int(m_big.group(1))
        print(f"  [CRT] x ≡ {x}, answer: {result}")
        send(str(result))
        data = read_all(3); print(data, end=''); continue
    more = read_all(5)
    if more: data = more; print(more, end='')
    else: break
s.close()
```
- So the flag is **flag{Ch1n3s3_m4th3m4t1c14n5_4r3_D0p3!}**
