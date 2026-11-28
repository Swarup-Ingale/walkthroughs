# URL
https://adventofcode.com/2019/day/16#part2#part2

# Description
--- Part Two ---

Now that your FFT is working, you can decode the real signal.

The real signal is your puzzle input repeated 10000 times. Treat this new signal as a single input list. Patterns are still calculated as before, and 100 phases of FFT are still applied.

The first seven digits of your initial input signal also represent the message offset. The message offset is the location of the eight-digit message in the final output list. Specifically, the message offset indicates the number of digits to skip before reading the eight-digit message. For example, if the first seven digits of your initial input signal were 1234567, the eight-digit message would be the eight digits after skipping 1,234,567 digits of the final output list. Or, if the message offset were 7 and your final output list were 98765432109876543210, the eight-digit message would be 21098765. (Of course, your real message offset will be a seven-digit number, not a one-digit number like 7.)

Here is the eight-digit message in the final output list after 100 phases. The message offset given in each input has been highlighted. (Note that the inputs given below are repeated 10000 times to find the actual starting input lists.)

03036732577212944063491565474664 becomes 84462026.
02935109699940807407585447034323 becomes 78725270.
03081770884921959731165446850517 becomes 53553731.

After repeating your input signal 10000 times and running 100 phases of FFT, what is the eight-digit message embedded in the final output list?

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
