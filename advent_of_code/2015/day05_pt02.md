# URL
https://adventofcode.com/2015/day/5#part2

# Description
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:
```
qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
```
How many strings are nice under these new rules?

# Method of Solve
This challenge can be solved by the below code:
  ```
    def is_nice(s):
    # Rule 1: pair appears twice without overlapping
    pair_twice = any(s[i:i+2] in s[i+2:] for i in range(len(s) - 1))

    # Rule 2: letter repeats with one in between
    repeat_with_gap = any(s[i] == s[i+2] for i in range(len(s) - 2))

    return pair_twice and repeat_with_gap


    count = 0
    with open("input_05_01") as f:
        for line in f:
            if is_nice(line.strip()):
                count += 1
    
    print(count)
  ```
This concludes the Day 05 of The Advent of Code
