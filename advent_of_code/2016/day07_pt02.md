# URL
https://adventofcode.com/2016/day/7#part2

# Description
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:
```
aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
```
How many IPs in your puzzle input support SSL?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    def get_aba_patterns(s):
        """
        Returns a set of (a, b) pairs for ABA patterns a b a where a != b
        """
        patterns = set()
        for i in range(len(s) - 2):
            a, b, c = s[i:i+3]
            if a == c and a != b:
                patterns.add((a, b))
        return patterns
    
    
    count = 0
    
    with open("input_07", "r") as f:
        for line in f:
            line = line.strip()
    
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
    
            abas = set()
            for s in supernets:
                abas |= get_aba_patterns(s)
    
            babs = set()
            for h in hypernets:
                for a, b in get_aba_patterns(h):
                    babs.add((b, a))  # reverse for BAB
    
            if abas & babs:
                count += 1
    
    print("Number of IPs that support SSL:", count)
  ```

# This Concludes the Day 07 of The Advent of Code.
