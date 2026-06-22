# URL
https://adventofcode.com/2018/day/18#part2

# Description
This important natural resource will need to last for at least thousands of years. Are the Elves collecting this lumber sustainably?

What will the total resource value of the lumber collection area be after 1000000000 minutes?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
grid = [
    list(line.strip())
    for line in open("input_18")
]

H = len(grid)
W = len(grid[0])

dirs = [
    (-1,-1),(0,-1),(1,-1),
    (-1,0),        (1,0),
    (-1,1),(0,1),(1,1)
]

seen = {}

minute = 0
TARGET = 1000000000

while minute < TARGET:

    key = "".join(
        "".join(r)
        for r in grid
    )

    if key in seen:

        cycle = minute - seen[key]

        remain = (
            TARGET - minute
        ) % cycle

        TARGET = minute + remain

    seen[key] = minute

    if minute == TARGET:
        break

    nxt = [r[:] for r in grid]

    for y in range(H):
        for x in range(W):

            trees = 0
            lumber = 0

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if not (
                    0 <= nx < W and
                    0 <= ny < H
                ):
                    continue

                if grid[ny][nx] == "|":
                    trees += 1

                elif grid[ny][nx] == "#":
                    lumber += 1

            if grid[y][x] == ".":
                if trees >= 3:
                    nxt[y][x] = "|"

            elif grid[y][x] == "|":
                if lumber >= 3:
                    nxt[y][x] = "#"

            else:
                if not (
                    trees >= 1 and
                    lumber >= 1
                ):
                    nxt[y][x] = "."

    grid = nxt
    minute += 1

trees = sum(
    row.count("|")
    for row in grid
)

lumber = sum(
    row.count("#")
    for row in grid
)

print(trees * lumber)
```
- The Javascript version is as follows:
```
const fs = require('fs');

let grid = fs.readFileSync('input_18','utf8')
    .trim()
    .split('\n')
    .map(r => r.split(''));

const H = grid.length;
const W = grid[0].length;

const dirs = [
    [-1,-1],[0,-1],[1,-1],
    [-1,0],       [1,0],
    [-1,1],[0,1],[1,1]
];

const seen = new Map();

let minute = 0;
const TARGET = 1000000000;

while (minute < TARGET) {

    const key =
        grid.map(r => r.join('')).join('');

    if (seen.has(key)) {

        const start = seen.get(key);
        const cycle = minute - start;

        const remain =
            (TARGET - minute) % cycle;

        for (let i = 0; i < remain; i++) {

            const next =
                grid.map(r => [...r]);

            for (let y = 0; y < H; y++) {
                for (let x = 0; x < W; x++) {

                    let trees = 0;
                    let lumber = 0;

                    for (const [dx,dy] of dirs) {

                        const nx = x + dx;
                        const ny = y + dy;

                        if (
                            nx < 0 || ny < 0 ||
                            nx >= W || ny >= H
                        ) continue;

                        if (grid[ny][nx] === '|')
                            trees++;

                        else if (grid[ny][nx] === '#')
                            lumber++;
                    }

                    if (
                        grid[y][x] === '.' &&
                        trees >= 3
                    )
                        next[y][x] = '|';

                    else if (
                        grid[y][x] === '|' &&
                        lumber >= 3
                    )
                        next[y][x] = '#';

                    else if (
                        grid[y][x] === '#'
                    ) {
                        if (!(trees >= 1 && lumber >= 1))
                            next[y][x] = '.';
                    }
                }
            }

            grid = next;
        }

        break;
    }

    seen.set(key, minute);

    const next =
        grid.map(r => [...r]);

    for (let y = 0; y < H; y++) {
        for (let x = 0; x < W; x++) {

            let trees = 0;
            let lumber = 0;

            for (const [dx,dy] of dirs) {

                const nx = x + dx;
                const ny = y + dy;

                if (
                    nx < 0 || ny < 0 ||
                    nx >= W || ny >= H
                ) continue;

                if (grid[ny][nx] === '|')
                    trees++;

                else if (grid[ny][nx] === '#')
                    lumber++;
            }

            if (
                grid[y][x] === '.' &&
                trees >= 3
            )
                next[y][x] = '|';

            else if (
                grid[y][x] === '|' &&
                lumber >= 3
            )
                next[y][x] = '#';

            else if (
                grid[y][x] === '#'
            ) {
                if (!(trees >= 1 && lumber >= 1))
                    next[y][x] = '.';
            }
        }
    }

    grid = next;
    minute++;
}

let trees = 0;
let lumber = 0;

for (const row of grid) {
    for (const c of row) {
        if (c === '|') trees++;
        if (c === '#') lumber++;
    }
}

console.log(trees * lumber);
```

# This Concludes Day 18 of The Advent of Code.
