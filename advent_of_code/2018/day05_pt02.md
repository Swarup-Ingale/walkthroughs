# URL
https://adventofcode.com/2018/day/5#part2

# Description
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:
```
    Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
    Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
    Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
    Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
```
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The python version is :
```
import string


def react(polymer):

    stack = []

    for unit in polymer:

        if (
            stack
            and stack[-1] != unit
            and stack[-1].lower() == unit.lower()
        ):
            stack.pop()
        else:
            stack.append(unit)

    return len(stack)


with open("input_05") as f:
    polymer = f.read().strip()

best = float('inf')

for letter in string.ascii_lowercase:

    filtered = ''.join(
        c
        for c in polymer
        if c.lower() != letter
    )

    best = min(
        best,
        react(filtered)
    )

print(best)
```
- The javascript version is :
```
const fs = require("fs");

const polymer = fs.readFileSync(
		'input_05',
		'utf-8'
		).trim();

function react (str) {
	const stack = [];
	for (const unit of str) {
		const top = stack [stack.length - 1];
		if ( top && top !== unit && top.toLowerCase() === unit.toLowerCase() ) {
			stack.pop();
		}
		else {
			stack.push(unit);
		}
	}
	return stack.length;
}

let best = Infinity;

for (let code = 97; code <= 122; code++) {
	const letter = String.fromCharCode(code);
	const filtered = [...polymer].filter ( c=> c.toLowerCase() !== letter ).join ('');
	best = Math.min( best, react(filtered) );
}

console.log(best);
```

# This Concludes The Day 05 of The Advent of Code.
