# URL
https://training.olicyber.it/challenges#challenge-288

# Concept
This challenge tests:

- **Binary data packing** — converting integers to little-endian byte sequences using `struct.pack` (equivalent to `p32`/`p64` from pwntools).
- **Network programming with raw sockets** — handling TCP stream buffering, parsing variable-length lines, and managing timeouts without relying on high-level libraries.
- **Latency-aware protocol implementation** — with a 30‑second global timer and ~270 ms RTT to the server, every millisecond matters; waiting for unnecessary delimiters or using blocking I/O inefficiently can push the client over the limit.

# Method of Solve

### 1. Early attempts

Initial attempts used `pwntools.recvuntil()` which introduced `EOFError` failures under load. Switching to a raw `socket` with `TCP_NODELAY` eliminated these inconsistencies.

### 2. The TCP fragmentation problem

The server sends each step's data in **two** TCP segments:

| Segment | Size | Content |
|---------|------|---------|
| 1       | ~52 B | `[+] Step N : restituiscimi 0xHEX packed a XX-bit\n` |
| 2       | ~14 B | `\n[+] Result : ` |

If the client waits for the full `\n[+] Result : ` separator before parsing, it wastes the time needed to receive the second segment. When RTT is already ~270 ms, an extra recv call per step pushes the total beyond 30 s.

### 3. Optimised approach

The key insight: the step line (segment 1) is **self-contained** — it contains both the hex value and the bit width. The `\n[+] Result :` trailing prompt is irrelevant for processing.

**Algorithm:**
```
for step in range(100):
    wait_until: buf contains "restituiscimi" AND a '\n' following it
    extract: hex value = line[14 : line.find(' ', 14)]
    extract: bit width = "64-bit" in line
    send: struct.pack("<Q", num) if 64-bit else struct.pack("<I", num)
    discard: buf = buf[nl+1:]
```

This halves the per-step recv calls: we process as soon as segment 1 arrives, without waiting for segment 2.

### 4. Parallel execution for reliability

Due to network jitter, some runs hit a slow TCP segment or a delayed ACK, causing a single step to take 400+ ms. Running **10 client instances in parallel** (using shell background jobs) significantly increases the chance of at least one instance seeing favourable network conditions.

### 5. Reaching the flag

With the optimised single-segment parsing, the average step time dropped to ~300–350 ms. Out of 10 parallel runs:

- **Run 5**: completed in 30.95 s — flag received
- **Run 8**: completed in 30.52 s — flag received
- Many others reached step 94–100 before the 30 s timer expired at 30.24 s.

## Final Script

```python
import socket, struct, sys, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect(('software-18.challs.olicyber.it', 13001))

buf = b''
while b'iniziare ...' not in buf:
    buf += s.recv(65536)

s.sendall(b'a\n')
buf = b''

for step in range(100):
    while True:
        ri = buf.find(b'restituiscimi ')
        if ri >= 0:
            nl = buf.find(b'\n', ri)
            if nl >= 0:
                break
        d = s.recv(65536)
        if not d:
            raise EOFError(f'step {step+1}')
        buf += d

    line = buf[ri:nl]
    hs = line[14:line.find(b' ', 14)]
    num = int(hs, 16)
    is64 = b'64-bit' in line
    buf = buf[nl+1:]
    s.sendall(struct.pack('<Q' if is64 else '<I', num))

time.sleep(1)
res = b''
s.settimeout(5)
try:
    while True:
        d = s.recv(65536)
        if not d:
            break
        res += d
except:
    pass
sys.stdout.buffer.write(res)
s.close()
```

## Flag

```
flag{ab2dde2a2b764d65}
```
- So the final flag is **flag{ab2dde2a2b764d65}**
