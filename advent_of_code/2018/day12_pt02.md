# URL
https://adventofcode.com/2018/day/12#part2

# Description
You realize that 20 generations aren't enough. After all, these plants will need to last another 1500 years to even reach your timeline, not to mention your future.

After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
TARGET = 50000000000

with open("input_12") as f:
    lines = [line.strip() for line in f]

state = lines[0].split(": ")[1]

rules = {}

for line in lines[2:]:

    if line:

        p, r = line.split(" => ")
        rules[p] = r

plants = {
    i
    for i, c in enumerate(state)
    if c == "#"
}

last_sum = sum(plants)
last_diff = None
stable = 0

for generation in range(1, 5000):

    next_plants = set()

    left = min(plants) - 2
    right = max(plants) + 2

    for pos in range(left, right + 1):

        pattern = ""

        for d in range(-2, 3):

            pattern += (
                "#"
                if pos + d in plants
                else "."
            )

        if rules.get(pattern) == "#":
            next_plants.add(pos)

    plants = next_plants

    current_sum = sum(plants)

    diff = current_sum - last_sum

    if diff == last_diff:
        stable += 1
    else:
        stable = 0

    if stable > 50:

        remaining = (
            TARGET
            - generation
        )

        answer = (
            current_sum
            + remaining * diff
        )

        print(answer)
        break

    last_sum = current_sum
    last_diff = diff
```
- The Javascript version of the code is as follows :
```
const fs = require('fs');

const TARGET =
    50000000000;

const lines = fs
    .readFileSync(
        'input_12',
        'utf8'
    )
    .trim()
    .split('\n');

const state =
    lines[0].split(': ')[1];

const rules = {};

for (const line of lines.slice(2)) {

    if (!line) continue;

    const [p, r] =
        line.split(' => ');

    rules[p] = r;
}

let plants = new Set();

for (
    let i = 0;
    i < state.length;
    i++
) {
    if (state[i] === '#')
        plants.add(i);
}

let lastSum =
    [...plants]
        .reduce((a, b) => a + b, 0);

let lastDiff = null;
let stable = 0;

for (
    let gen = 1;
    gen < 5000;
    gen++
) {

    const next =
        new Set();

    const values =
        [...plants];

    const min =
        Math.min(...values);

    const max =
        Math.max(...values);

    for (
        let pos = min - 2;
        pos <= max + 2;
        pos++
    ) {

        let pattern = '';

        for (
            let d = -2;
            d <= 2;
            d++
        ) {
            pattern +=
                plants.has(pos + d)
                    ? '#'
                    : '.';
        }

        if (
            rules[pattern] === '#'
        ) {
            next.add(pos);
        }
    }

    plants = next;

    const currentSum =
        [...plants]
            .reduce(
                (a, b) => a + b,
                0
            );

    const diff =
        currentSum - lastSum;

    if (diff === lastDiff)
        stable++;
    else
        stable = 0;

    if (stable > 50) {

        const remaining =
            TARGET - gen;

        console.log(
            currentSum +
            remaining * diff
        );

        break;
    }

    lastSum = currentSum;
    lastDiff = diff;
}
```

# This Concludes Day 12 of The Advent of Code.
