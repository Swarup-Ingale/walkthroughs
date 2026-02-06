# URL
https://adventofcode.com/2015/day/11

# Description
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:
```
hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
```
Given Santa's current password (your puzzle input), what should his next password be?

# Method of Solve
- The part 01 of the challenge can be solved using the code given below:
  ```
    def increment_password(pw):
    pw = list(pw)
    i = len(pw) - 1

    while i >= 0:
        if pw[i] == 'z':
            pw[i] = 'a'
            i -= 1
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break

    return ''.join(pw)


    def has_straight(pw):
        for i in range(len(pw) - 2):
            a, b, c = pw[i], pw[i+1], pw[i+2]
            if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
                return True
        return False
    
    
    def has_no_invalid_letters(pw):
        return not any(c in pw for c in "iol")
    
    
    def has_two_pairs(pw):
        pairs = set()
        i = 0
        while i < len(pw) - 1:
            if pw[i] == pw[i + 1]:
                pairs.add(pw[i])
                i += 2  			# skip to avoid overlap
            else:
                i += 1
        return len(pairs) >= 2
    
    
    def is_valid(pw):
        return (
            has_straight(pw)
            and has_no_invalid_letters(pw)
            and has_two_pairs(pw)
        )
    
    
    with open("input_11_01", "r") as f:
        password = f.read().strip()
    
    while True:
        password = increment_password(password)
        if is_valid(password):
            print(password)
            break
  ```

# This is Solution for part 01 of the challenge
