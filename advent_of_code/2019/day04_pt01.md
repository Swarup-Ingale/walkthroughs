# URL
https://adventofcode.com/2019/day/4

# Description
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:
```
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
```
Other than the range rule, the following are true:
```
    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).
```
How many different passwords within the range given in your puzzle input meet these criteria?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input04", "r") as f:
	start, end = map(int, f.read().strip().split("-"))

def valid(password):
	s = str(password)

	has_double = False

	for i in range(5):
		if s[i] == s[i + 1]:
			has_double = True

		if s[i] > s[i + 1]:
			return False

	return has_double

count = sum(valid(n) for n in range(start, end + 1))

print(count)
```
- The Javascript version is as follows:
```
const fs = require("fs");

const [start, end] = fs
	.readFileSync("input04", "utf-8")
	.trim()
	.split("-")
	.map(Number);

function valid(password) {
	const s = String(password);

	let hasDouble = false;

	for (let i = 0; i < 5; i++) {
		if (s[i] === s[i + 1]) {
			hasDouble = true;
		}

		if (s[i] > s[i + 1]) {
			return false;
		}
	}

	return hasDouble;
}

let count = 0;

for (let i = start; i <= end; i++) {
	if (valid(i)) {
		count ++;
	}
}

console.log(count);
```
- This Solves The Part 01 of this challenge.
