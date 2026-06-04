# URL
https://training.olicyber.it/challenges#challenge-339

# Concept

Interactive tutorial on PyCryptodome covering hash functions (SHA3-384, SHA-224), HMAC, DSA key parsing (non-standard DER format), prime generation, and Miller-Rabin primality testing.

# Method of Solve

- First question: compute SHA3-384 hash of `hash_me_pls`

```
from Crypto.Hash import SHA3_384
h = SHA3_384.new(b'hash_me_pls')
h.hexdigest()
```

- Second question: compute HMAC-SHA-224 with given hex key

```
from Crypto.Hash import HMAC, SHA224
key = bytes.fromhex(key_hex)
msg = b'La mia integrit\xc3\xa0 \xc3\xa8 importante!'
HMAC.new(key, msg, SHA224).hexdigest()
```

- DSA questions: parse the non-standard DER-encoded DSA private key using pyasn1 (the structure is `SEQUENCE{ version, SEQUENCE{OID, SEQUENCE{p,q,g}}, OCTET STRING{INTEGER x} }`)

```
from pyasn1.codec.der import decoder
decoded, _ = decoder.decode(bytes.fromhex(key_hex))
params = decoded[1][1]
p, q, g = int(params[0]), int(params[1]), int(params[2])
inner = decoder.decode(decoded[2].asOctets())[0]
x = int(inner)
y = pow(g, x, p)
```

- Answer multiple DSA component queries (q, x, y, p, g) caching the parsed key for reuse since the hex key is sent once
- Prime generation: `number.getPrime(bits)` from `Crypto.Util.number`
- Primality test: `number.isPrime(p)` — answer `"si"` or `"no"`

# Final Script

```python
import socket, re, time
from Crypto.Hash import SHA3_384, SHA384, SHA256, SHA224, MD5, SHA1, HMAC
from Crypto.PublicKey import RSA, DSA, ECC
from Crypto.Util import number
from pyasn1.codec.der import decoder as der_decoder

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)
s.connect(('cr14.challs.olicyber.it', 30007))

def recv_until_prompt():
    buf = b""
    s.settimeout(6)
    while True:
        try:
            d = s.recv(4096)
            if not d: break
            buf += d
            txt = buf.decode(errors='ignore')
            if '?' in txt or 'flag{' in txt or 'errato' in txt or 'sbagliata' in txt: break
        except socket.timeout: break
    s.settimeout(30)
    return buf.decode(errors='ignore')

def send(t):
    s.sendall((str(t) + '\n').encode())
    time.sleep(0.3)

hash_algs = {
    'SHA3-384': SHA3_384, 'SHA384': SHA384, 'SHA256': SHA256,
    'SHA224': SHA224, 'SHA-224': SHA224, 'SHA-256': SHA256,
    'SHA-384': SHA384, 'SHA-1': SHA1, 'SHA1': SHA1, 'MD5': MD5
}

dsa_key = None

def dsa_parse(hex_str):
    data = bytes.fromhex(hex_str)
    decoded, _ = der_decoder.decode(data)
    params = decoded[1][1]
    p, q, g = int(params[0]), int(params[1]), int(params[2])
    inner = der_decoder.decode(decoded[2].asOctets())[0]
    x = int(inner)
    y = pow(g, x, p)
    return {'y': y, 'g': g, 'p': p, 'q': q, 'x': x}

vars_map = {}
data = recv_until_prompt()
print(data, end='', flush=True)

while True:
    if 'flag{' in data:
        m = re.search(r'flag\{[^}]+\}', data)
        print(f"\nFLAG: {m.group()}")
        break
    if 'errato' in data or 'sbagliata' in data:
        print("Wrong!")
        break

    for m in re.finditer(r"(\w+)\s*=\s*'([^']*)'", data):
        vars_map[m.group(1)] = m.group(2)

    def resolve(val):
        return vars_map.get(val, val)

    # HMAC
    m = re.search(r"Hash to use = ([\w-]+)", data)
    if m:
        hash_name = m.group(1)
        m_key = re.search(r"(\w+)\.hex\(\)\s*=\s*'([0-9a-fA-F]+)'", data)
        m_msg = re.search(r"msg\s*=\s*'([^']*)'", data)
        if m_key and m_msg and 'HMAC' in data:
            key = bytes.fromhex(m_key.group(2))
            msg = m_msg.group(1).encode()
            h = HMAC.new(key, msg, hash_algs[hash_name])
            send(h.hexdigest())
            time.sleep(1)
            data = recv_until_prompt()
            print(data, end='', flush=True)
            continue

    # DSA
    m_key = re.search(r"key_?\.hex\(\)\s*=\s*'([0-9a-fA-F]+)'", data)
    if m_key: dsa_key = dsa_parse(m_key.group(1))
    m2 = re.search(r"(y|g|p|q|x)\s*=\s*\?", data)
    if m2 and dsa_key:
        send(dsa_key[m2.group(1)])
        time.sleep(1)
        data = recv_until_prompt()
        print(data, end='', flush=True)
        continue

    # Hash functions
    matched = False
    for h_name, h_class in hash_algs.items():
        m = re.search(rf"{h_name}\((\w+)\)\s*=\s*\?\s*\(hex\)", data)
        if m:
            msg = resolve(m.group(1))
            h = h_class.new(msg.encode() if isinstance(msg, str) else msg)
            send(h.hexdigest())
            time.sleep(1)
            data = recv_until_prompt()
            print(data, end='', flush=True)
            matched = True
            break
        m = re.search(rf"{h_name}\('([^']+)'\)\s*=\s*\?\s*\(hex\)", data)
        if m:
            h = h_class.new(m.group(1).encode())
            send(h.hexdigest())
            time.sleep(1)
            data = recv_until_prompt()
            print(data, end='', flush=True)
            matched = True
            break
    if matched: continue

    # Prime generation
    m = re.search(r"(?:primo|prime|numero primo).*?(\d+)\s*bits?", data, re.IGNORECASE)
    if m:
        send(number.getPrime(int(m.group(1))))
        time.sleep(1)
        data = recv_until_prompt()
        print(data, end='', flush=True)
        continue

    # Primality test
    m = re.search(r"p\s*=\s*(\d+)", data)
    if m and ('primo' in data or 'prime' in data):
        send("si" if number.isPrime(int(m.group(1))) else "no")
        time.sleep(1)
        data = recv_until_prompt()
        print(data, end='', flush=True)
        continue

    send("0")
    time.sleep(1)
    data = recv_until_prompt()
    print(data, end='', flush=True)

s.close()
```
- The flag is **flag{kn0w1n6_(h0w_to_us3_A_l1Br4Ry)_i$_h4lf_th3_B4Tt1e}**
