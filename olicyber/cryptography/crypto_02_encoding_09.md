# URL
https://training.olicyber.it/challenges#challenge-334

# Concept
Using the Extended Euclidean Algorithm to compute modular inverses and answer questions about modular arithmetic.

# Method of Solve
- Connect to the remote service:
  ```
  nc crypto-09.challs.olicyber.it 30002
  ```
- Three types of questions are asked in sequence:
  1. **Bezout coefficients**: Given `a` and `b`, find `x, y` such that `x*a + y*b = GCD(a,b)` — solve with Extended Euclidean Algorithm
  2. **Invertibility check**: Given `a` and `n`, determine if `a` is invertible modulo `n` — yes iff `GCD(a, n) = 1`
  3. **Modular inverse**: Given `a` and `n`, compute the modular inverse `a⁻¹ mod n` — use Extended Euclidean Algorithm and take `x mod n`
- Example — Bezout for `a=124, b=159`:
  ```
  extended_gcd(124, 159) = (1, -50, 39)
  Check: -50*124 + 39*159 = -6200 + 6201 = 1 ✓
  Send: x=-50, y=39
  ```
- Example — Invertibility for `124 mod 159`:
  ```
  GCD(124, 159) = 1 → invertible → send "si"
  ```
- Example — Inverse of `53 mod 124`:
  ```
  extended_gcd(53, 124) = (1, 117, -50)
  Inverse: 117 mod 124 = 117
  Send: 117
  ```

# Final Script
```python
import socket, re, time

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('crypto-09.challs.olicyber.it', 30002))
s.settimeout(30)

def read_all(timeout=2):
    buf = b""
    s.settimeout(timeout)
    while True:
        try:
            data = s.recv(4096)
            if not data:
                break
            buf += data
        except socket.timeout:
            break
    s.settimeout(30)
    return buf.decode(errors='ignore')

def send_line(text):
    s.sendall((text + '\n').encode())
    time.sleep(0.2)

data = read_all(3)
print(data, end='')

while True:
    if 'flag{' in data:
        m = re.search(r'flag\{[^}]+\}', data)
        print(f"\n[+] FLAG: {m.group()}")
        break

    # Bezout
    m = re.search(r'a = (\d+), b = (\d+).*?x \= \?', data, re.DOTALL)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        g, x, y = extended_gcd(a, b)
        send_line(str(x))
        read_all(1)
        send_line(str(y))
        data = read_all(2)
        print(data, end='')
        continue

    # Invertibility
    m = re.search(r'(\d+) è invertibile mod (\d+)', data)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        g, _, _ = extended_gcd(a, b)
        send_line('si' if g == 1 else 'no')
        data = read_all(2)
        print(data, end='')
        continue

    # Modular inverse
    m = re.search(r'inverso di (\d+) mod(?:ulo)? (\d+)', data)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        g, x, _ = extended_gcd(a, b)
        send_line(str(x % b))
        data = read_all(2)
        print(data, end='')
        continue

    more = read_all(3)
    if more:
        data = more
        print(more, end='')
    else:
        break

s.close()
```
- The final flag is **flag{m3an1Ng_is_4l1_4b0uT_C0nT3xt}**
