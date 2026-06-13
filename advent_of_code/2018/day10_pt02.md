# URL
https://adventofcode.com/2018/day/10#part2

# Description
Good thing you didn't have to wait, because that would have taken a long time - much longer than the 3 seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious: exactly how many seconds would they have needed to wait for that message to appear?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re

points = []

with open("input_10") as f:
    for line in f:
        points.append(
            list(
                map(
                    int,
                    re.findall(
                        r"-?\d+",
                        line
                    )
                )
            )
        )


def area(points):

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    return (
        max(xs) - min(xs)
    ) * (
        max(ys) - min(ys)
    )


best_area = float("inf")
best_time = 0

for t in range(20000):

    current = area(points)

    if current < best_area:

        best_area = current
        best_time = t

    for p in points:
        p[0] += p[2]
        p[1] += p[3]

print(best_time)
```
- The Javascript version is as follows:
```
const fs = require('fs');

const points = fs
    .readFileSync('input_10', 'utf8')
    .trim()
    .split('\n')
    .map(line =>
        line.match(/-?\d+/g)
            .map(Number)
    );

function area(points) {

    const xs =
        points.map(p => p[0]);

    const ys =
        points.map(p => p[1]);

    return (
        Math.max(...xs) -
        Math.min(...xs)
    ) *
    (
        Math.max(...ys) -
        Math.min(...ys)
    );
}

let bestArea =
    Number.MAX_SAFE_INTEGER;

let bestTime = 0;

for (
    let t = 0;
    t < 20000;
    t++
) {

    const current =
        area(points);

    if (
        current < bestArea
    ) {

        bestArea = current;
        bestTime = t;
    }

    for (const p of points) {

        p[0] += p[2];
        p[1] += p[3];
    }
}

console.log(bestTime);
```

# This Concludes the Day 10 of The Advent of Code.
