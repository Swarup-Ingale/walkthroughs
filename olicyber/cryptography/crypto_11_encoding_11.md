# URL
https://training.olicyber.it/challenges#challenge-336

# Concept
Interactive RSA tutorial — compute `n`, `ϕ(n)`, choose `e`, compute `c = m^e mod n`, and find `d = e⁻¹ mod ϕ(n)`.

# Method of Solve
- Connect: `nc crypto-11.challs.olicyber.it 30004`
- For each step:
  1. **n = p × q** — given two primes
  2. **m** — choose any number coprime with `n` (e.g. `2`)
  3. **ϕ(n) = (p-1)(q-1)** — Euler's totient
  4. **e** — choose any `1 < e < ϕ(n)` with `GCD(e, ϕ(n)) = 1`
  5. **c = m^e mod n** — modular exponentiation via `pow(m, e, n)`
  6. **d = e⁻¹ mod ϕ(n)** — modular inverse via Extended Euclidean Algorithm
  7. **m = c^d mod n** — verify decryption

# Final Script
```python
import socket, re, time

def egcd(a, b):
    if b == 0: return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect(('crypto-11.challs.olicyber.it', 30004))

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
    s.settimeout(10)
    return buf

def send(t):
    s.sendall((str(t) + '\n').encode())
    time.sleep(0.3)

p = q = n = phi = e = None
m_val = None

data = recv_until(b'? ')
print(data.decode(errors='ignore'), end='')

while True:
    txt = data.decode(errors='ignore')

    if 'flag{' in txt:
        m = re.search(r'flag\{[^}]+\}', txt)
        print(f"\n[+] FLAG: {m.group()}"); break
    if 'errato' in txt or 'sbagliata' in txt:
        print("[-] Wrong!"); break

    m_ = re.search(r'p = (\d+), q = (\d+)', txt)
    if m_ and 'n = ?' in txt:
        p, q = int(m_.group(1)), int(m_.group(2))
        n = p * q; phi = (p-1)*(q-1)
        print(f"  n = {n}"); send(n)

    elif 'm = ?' in txt:
        m_val = 2
        while egcd(m_val, n)[0] != 1: m_val += 1
        print(f"  m = {m_val}"); send(m_val)

    elif re.search(r'[ϕφ]\(n\)\s*=\s*\?|phi\(n\)\s*=\s*\?', txt):
        print(f"  phi = {phi}"); send(phi)

    elif 'e = ?' in txt:
        for ev in range(3, phi):
            if egcd(ev, phi)[0] == 1: e = ev; break
        print(f"  e = {e}"); send(e)

    elif 'c = ?' in txt or "c = m^e" in txt:
        c = pow(m_val, e, n)
        print(f"  c = {c}"); send(c)

    elif 'd = ?' in txt:
        _, d, _ = egcd(e, phi)
        d = d % phi
        print(f"  d = {d}"); send(d)

    elif '= ?' in txt:
        mp = re.search(r'(\d+)\^(\d+) mod (\d+)', txt)
        if mp:
            r = pow(int(mp.group(1)), int(mp.group(2)), int(mp.group(3)))
            print(f"  {mp.group(1)}^{mp.group(2)} mod {mp.group(3)} = {r}")
            send(r)
        else:
            send("0")

    else:
        data = recv_until(b'? ', timeout=5)
        if data:
            print(data.decode(errors='ignore'), end='')
            continue
        else:
            break

    data = recv_until(b'? ', timeout=5)
    if data:
        print(data.decode(errors='ignore'), end='')
    else:
        break

s.close()
```
- The flag is **flag{RSA_n0n_f4_p1u_C0s1_p4Ur4}**
