# URL
https://adventofcode.com/2017/day/9#part2

# Description
Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.
```
<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
```
How many non-canceled characters are within the garbage in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
with open("input_09", "r") as f:
    stream = f.read().strip()

garbage = False
skip = False
garbage_count = 0

for c in stream:

    if skip:
        skip = False
        continue

    if c == "!":
        skip = True
        continue

    if garbage:
        if c == ">":
            garbage = False
        else:
            garbage_count += 1
        continue

    if c == "<":
        garbage = True

print(garbage_count)
```

# This Concludes Day 09 of The Advent of Code.
