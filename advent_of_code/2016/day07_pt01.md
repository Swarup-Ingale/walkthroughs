# URL
https://adventofcode.com/2016/day/7

# Description
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:
```
abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
```
How many IPs in your puzzle input support TLS?

# Method of Solve
- The part 01 of this challenge can be solved using the following code:
  ```
    def has_abba(s):
        """
        Returns True if string s contains an ABBA pattern.
        """
        for i in range(len(s) - 3):
            a, b, c, d = s[i:i+4]
            if a != b and a == d and b == c:
                return True
        return False
    
    
    count = 0
    
    with open("input_07", "r") as f:
        for line in f:
            line = line.strip()
    
            # Split into supernet and hypernet sequences
            parts = []
            temp = ""
            in_brackets = False
    
            for ch in line:
                if ch == "[":
                    parts.append((temp, in_brackets))
                    temp = ""
                    in_brackets = True
                elif ch == "]":
                    parts.append((temp, in_brackets))
                    temp = ""
                    in_brackets = False
                else:
                    temp += ch
    
            parts.append((temp, in_brackets))
    
            supernets = [p for p, b in parts if not b]
            hypernets = [p for p, b in parts if b]
    
            # Check rules
            if any(has_abba(s) for s in supernets) and not any(has_abba(h) for h in hypernets):
                count += 1
    
    print("Number of IPs that support TLS:", count)
  ```
- This Solves the part 01 of the challenge.
