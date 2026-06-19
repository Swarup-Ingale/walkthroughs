# URL
https://adventofcode.com/2018/day/17#Part02

# Description
After a very long time, the water spring will run dry. How much water will be retained?

In the example above, water that won't eventually drain out is shown as ~, a total of 29 tiles.

How many water tiles are left after the water spring stops producing water and all remaining water not at rest has drained?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Javascript version is as follows:
```
const fs = require('fs');

const lines = fs.readFileSync('input_17', 'utf8').trim().split('\n');

const clay = new Set();

let minY = Infinity;
let maxY = -Infinity;

for (const line of lines) {

    const nums = [...line.matchAll(/\d+/g)]
        .map(x => Number(x[0]));

    if (line.startsWith('x=')) {

        const [x, y1, y2] = nums;

        for (let y = y1; y <= y2; y++) {
            clay.add(`${x},${y}`);
        }

        minY = Math.min(minY, y1);
        maxY = Math.max(maxY, y2);

    } else {

        const [y, x1, x2] = nums;

        for (let x = x1; x <= x2; x++) {
            clay.add(`${x},${y}`);
        }

        minY = Math.min(minY, y);
        maxY = Math.max(maxY, y);
    }
}

const water = new Set();
const settled = new Set();

function blocked(x, y) {
    return clay.has(`${x},${y}`) ||
           settled.has(`${x},${y}`);
}

function fill(x, y) {

    if (y > maxY) return;

    const k = `${x},${y}`;

    if (
        water.has(k) ||
        blocked(x, y)
    ) return;

    water.add(k);

    fill(x, y + 1);

    if (!blocked(x, y + 1))
        return;

    let left = x;
    let right = x;

    let leftWall = false;
    let rightWall = false;

    while (true) {

        left--;

        if (clay.has(`${left},${y}`)) {
            leftWall = true;
            break;
        }

        water.add(`${left},${y}`);

        if (!blocked(left, y + 1)) {
            fill(left, y + 1);

            if (!blocked(left, y + 1))
                break;
        }
    }

    while (true) {

        right++;

        if (clay.has(`${right},${y}`)) {
            rightWall = true;
            break;
        }

        water.add(`${right},${y}`);

        if (!blocked(right, y + 1)) {
            fill(right, y + 1);

            if (!blocked(right, y + 1))
                break;
        }
    }

    if (leftWall && rightWall) {

        for (
            let xx = left + 1;
            xx < right;
            xx++
        ) {

            settled.add(`${xx},${y}`);
        }

        fill(x, y - 1);
    }
}

fill(500, 0);

let part1 = 0;
let part2 = 0;

for (const p of water) {

    const y =
        Number(
            p.split(',')[1]
        );

    if (
        y >= minY &&
        y <= maxY
    ) {
        part1++;
    }
}

for (const p of settled) {

    const y =
        Number(
            p.split(',')[1]
        );

    if (
        y >= minY &&
        y <= maxY
    ) {
        part2++;
    }
}

console.log('Part 1:', part1);
console.log('Part 2:', part2);
```

# This Concludes Day 17 of The Advent of Code.
