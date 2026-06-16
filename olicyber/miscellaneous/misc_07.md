# URL
https://training.olicyber.it/challenges#challenge-710

# Concept
To understand Basics of Bash Scripting

# Method of Solve
- The Python script I used is as follows:
```
timeout 15 python3 << 'PYEOF'
import socket, time

s = socket.socket()
s.settimeout(5)
s.connect(('basicbash.challs.olicyber.it', 38048))
time.sleep(0.3)

def recv_all():
    data = b''
    s.settimeout(1)
    while True:
        try:
            chunk = s.recv(4096)
            if not chunk: break
            data += chunk
        except: break
    s.settimeout(5)
    return data.decode(errors='replace')

def send(cmd):
    s.sendall((cmd + '\n').encode())
    time.sleep(0.3)
    return recv_all()

# Navigate to first alphabetical folder: cartella
print("=== cd cartella ===")
print(send('cd cartella'))

print("=== ls -la cartella ===")
print(send('ls -la'))

# Find .esempio size
print("=== ls -la .esempio ===")
print(send('ls -la .esempio'))

# Print gatto content
print("=== cat gatto ===")
print(send('cat gatto'))

# File info on eseguibile
print("=== file eseguibile ===")
print(send('file eseguibile'))

# Run eseguibile
print("=== ./eseguibile ===")
print(send('./eseguibile'))

# Navigate to sottocartella
print("=== cd sottocartella ===")
print(send('cd sottocartella'))

print("=== ls ===")
print(send('ls'))

# Search for olicyber
print("=== grep -r olicyber ===")
print(send('grep -r olicyber'))

s.close()
PYEOF
```

# Flag
```
flag{109_ffeaf8a1a4a9a9ef_banananana_9e8b1fd8f180b627}
```
- So the final flag is **flag{109_ffeaf8a1a4a9a9ef_banananana_9e8b1fd8f180b627}**
