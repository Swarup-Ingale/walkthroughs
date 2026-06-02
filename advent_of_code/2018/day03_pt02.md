# URL
https://adventofcode.com/2018/day/3#part2

# Description
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code :
- The Python version is :
```
import re
from collections import defaultdict

fabric = defaultdict(int)
claims = []

with open("input_03") as f:
    for line in f:

        claim = tuple(
            map(
                int,
                re.match(
                    r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",
                    line.strip()
                ).groups()
            )
        )

        claims.append(claim)

        cid, x, y, w, h = claim

        for i in range(x, x + w):
            for j in range(y, y + h):
                fabric[(i, j)] += 1

for cid, x, y, w, h in claims:

    clean = True

    for i in range(x, x + w):
        for j in range(y, y + h):

            if fabric[(i, j)] > 1:
                clean = False
                break

        if not clean:
            break

    if clean:
        print(cid)
        break
```
- The Javascript version is :
```
const fs = require('fs');

const lines = fs
    .readFileSync('input_03', 'utf8')
    .trim()
    .split('\n');

const fabric = new Map();
const claims = [];

for (const line of lines) {

    const match =
        line.match(
            /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/
        );

    const [,
        id,
        x,
        y,
        w,
        h
    ] = match.map(Number);

    claims.push({ id, x, y, w, h });

    for (let i = x; i < x + w; i++) {
        for (let j = y; j < y + h; j++) {

            const key = `${i},${j}`;

            fabric.set(
                key,
                (fabric.get(key) || 0) + 1
            );
        }
    }
}

for (const claim of claims) {

    let clean = true;

    for (
        let i = claim.x;
        i < claim.x + claim.w;
        i++
    ) {
        for (
            let j = claim.y;
            j < claim.y + claim.h;
            j++
        ) {

            const key = `${i},${j}`;

            if (fabric.get(key) > 1) {
                clean = false;
                break;
            }
        }

        if (!clean) break;
    }

    if (clean) {
        console.log(claim.id);
        break;
    }
}
```

# This Concludes The Day 03 of The Advent of Code.
