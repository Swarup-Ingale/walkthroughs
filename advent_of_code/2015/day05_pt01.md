# URL
https://adventofcode.com/2015/day/5

# Description
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:
```
ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
```
How many strings are nice?

# Method of Solve
The below code is the solution for solving part 01 of this Challenge:
  ```
    def is_nice(s):
    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]

    # Rule 1: at least 3 vowels
    vowel_count = sum(1 for c in s if c in vowels)
    if vowel_count < 3:
        return False

    # Rule 2: at least one double letter
    has_double = any(s[i] == s[i+1] for i in range(len(s)-1))
    if not has_double:
        return False

    # Rule 3: no forbidden substrings
    if any(bad in s for bad in forbidden):
        return False

    return True


    count = 0
    with open("input_05_01") as f:
        for line in f:
            if is_nice(line.strip()):
                count += 1
    
    print(count)
```
This Solves the part 01 of the challenge
