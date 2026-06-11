# URL
https://training.olicyber.it/challenges#challenge-287

# Concept
`pwntools` is a Python library for CTF exploitation and binary interaction. It provides `remote()` for socket connections, `recvuntil()` for pattern-based receiving, and `sendline()` for sending data. This challenge requires connecting to a remote server, solving 10 arithmetic sums within 10 seconds, and receiving the flag.

# Method of Solve
1. **Connect** to the remote service:
   ```python
   from pwn import *
   r = remote("software-17.challs.olicyber.it", 13000)
   ```

2. **Receive** the welcome message and send any character to start.

3. **Loop 10 times**: receive data until `"Somma? : "`, parse the list of numbers (using `rfind("[")` to locate the actual number list, avoiding the step header), compute the sum, and send it.

4. **Receive the flag** after all 10 steps.

```python
for _ in range(10):
    data = r.recvuntil(b"Somma? : ", timeout=10)
    idx = data.rfind(b"[")
    list_part = data[idx:]
    nums = re.findall(rb"-?\d+", list_part)
    nums = [int(n) for n in nums]
    r.sendline(str(sum(nums)).encode())

print(r.recvall(timeout=5).decode())
```

# Flag
`flag{455b7c904a9fb4a6}`
- So the final flag is **flag{455b7c904a9fb4a6}**
