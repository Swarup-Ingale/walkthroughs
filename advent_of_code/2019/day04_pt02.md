# URL
https://adventofcode.com/2019/day/4#part2

# Description
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:
```
    112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
```
How many different passwords within the range given in your puzzle input meet all of the criteria?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Python version is as follows:
```
from collections import Counter

with open("input04", "r") as f:
	start, end = map(int, f.read().strip().split("-"))

def valid(password):
	s = str(password)

	for i in range(5):
		if s[i] > s[i + 1]:
			return False

	counts = Counter(s)

	return 2 in counts.values()

count = sum(valid(n) for n in range(start, end + 1))

print(count)
```
- The Javascript version is as follows:
```
const fs = require("fs");

const [start, end] = fs
    .readFileSync("input04", "utf8")
    .trim()
    .split("-")
    .map(Number);

function valid(password) {
    const s = String(password);

    for (let i = 0; i < 5; i++) {
        if (s[i] > s[i + 1]) {
            return false;
        }
    }

    const counts = {};

    for (const ch of s) {
        counts[ch] = (counts[ch] || 0) + 1;
    }

    return Object.values(counts).includes(2);
}

let count = 0;

for (let i = start; i <= end; i++) {
    if (valid(i)) {
        count++;
    }
}

console.log(count);
```

# This Concludes Day 04 of The Advent of Code.
