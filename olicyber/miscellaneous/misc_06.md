# URL
https://training.olicyber.it/challenges#challenge-253

# Concept 
To understand regular expressions and how to solve them

# Method of Solve
- I wrote a python script to solve the regex using the re module of python
```
import re, random, string

pattern = r'^flag\{[\D]{2}[0][a-z][^0-9][L][\w]{4}[^a-pr-z]{3}[^\d]{2}[\d][b]\}$'

def generate():
    # [\D]{2} - two non-digits
    p2 = ''.join(random.choice(string.ascii_letters) for _ in range(2))
    # [0]
    p3 = '0'
    # [a-z] - one lowercase
    p4 = random.choice(string.ascii_lowercase)
    # [^0-9] - one non-digit
    p5 = random.choice(string.ascii_letters + string.punctuation)
    # [L]
    p6 = 'L'
    # [\w]{4} - four word chars
    p7 = ''.join(random.choice(string.ascii_letters + string.digits + '_') for _ in range(4))
    # [^a-pr-z]{3} - only 'q' qualifies
    p8 = 'qqq'
    # [^\d]{2} - two non-digits
    p9 = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(2))
    # [\d] - one digit
    p10 = random.choice(string.digits)
    # [b]
    p11 = 'b'
    flag = f'flag{{{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}{p11}}}'
    assert re.match(pattern, flag), f'generation failed: {flag}'
    return flag

print(generate())
```
- Also the proper breakdown is :
```
- [\D]{2} → two non-digits (e.g. ab)
- [0] → literal 0
- [a-z] → one lowercase letter
- [^0-9] → one non-digit
- [L] → literal L
- [\w]{4} → four word chars
- [^a-pr-z]{3} → three q's (the only lowercase letter not in a-p or r-z)
- [^\d]{2} → two non-digits
- [\d] → one digit
- [b] → literal b
```

# Flag
```
flag{ab0x!Labcdqqq!!1b}
```
- So the final flag is **flag{ab0x!Labcdqqq!!1b}**
