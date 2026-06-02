# URL
https://adventofcode.com/2018/day/3

# Description
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
```
    The number of inches between the left edge of the fabric and the left edge of the rectangle.
    The number of inches between the top edge of the fabric and the top edge of the rectangle.
    The width of the rectangle in inches.
    The height of the rectangle in inches.
```
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
```
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
```
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
```
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
```
Visually, these claim the following areas:
```
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
```
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python Version is :
```
import re
from collections import defaultdict

fabric = defaultdict(int)

with open("input_03") as f:
    for line in f:
        claim_id, x, y, w, h = map(
            int,
            re.match(
                r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",
                line.strip()
            ).groups()
        )

        for i in range(x, x + w):
            for j in range(y, y + h):
                fabric[(i, j)] += 1

overlap = sum(1 for count in fabric.values() if count >= 2)

print(overlap)
```
- The Javascript Version is :
```
const fs = require('fs');

const lines = fs
    .readFileSync('input_03', 'utf8')
    .trim()
    .split('\n');

const fabric = new Map();

for (const line of lines) {

    const match = line.match(
        /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/
    );

    const [, id, x, y, w, h] =
        match.map(Number);

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

let overlap = 0;

for (const count of fabric.values()) {
    if (count >= 2) overlap++;
}

console.log(overlap);
```
- This solves the Part 01 of this challenge.
