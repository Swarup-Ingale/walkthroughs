# URL
https://adventofcode.com/2019/day/16/answer#part2

# Description
Description not found.

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```python
with open("input16", "r") as f:
	original = list(map(int, f.read().strip()))

offset = int("".join(map(str, original[:7])))

total_length = len(original) * 10000

if offset < total_length // 2:
	raise ValueError("Error in offset, it must be in the second half of the signal")
signal = (original * 10000)[offset:]

for phase in range(100):
	total = 0
	for i in range(len(signal) - 1, -1, -1):
		total += signal[i]
		signal[i] = total % 10

answer = "".join(map(str, signal[:8]))

print(f"part 2 solution is : {answer}")
```
- The JavaScript version is as follows:
```javascript
const fs = require("fs");

const original = fs.readFileSync("input16", "utf-8").trim().split("").map(Number);
const offset = Number(original.slice(0, 7).join(""));
const totalLength = original.length * 10000;


if (offset < Math.floor(totalLength / 2)) {
	throw new Error("offset must be in the second half of the signal.");
}

const signal = Array.from({ length: totalLength - offset }, (_, i) => original[(offset + i) % original.length]);

for (let phase = 0; phase < 100; phase++) {

	let total = 0;

	for (let i = signal.length - 1; i >= 0; i--) {

		total += signal[i];

		signal[i] = total % 10;
	}
}


const answer = signal
	.slice(0, 8)
	.join("");


console.log(`Part 2: ${answer}`);
```
- This Concludes Day 16 of The Advent of Code.
