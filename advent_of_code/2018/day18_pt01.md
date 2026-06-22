# URL
https://adventofcode.com/2018/day/18

# Description
On the outskirts of the North Pole base construction project, many Elves are collecting lumber.

The lumber collection area is 50 acres by 50 acres; each acre can be either open ground (.), trees (|), or a lumberyard (#). You take a scan of the area (your puzzle input).

Strange magic is at work here: each minute, the landscape looks entirely different. In exactly one minute, an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to open ground (the lumber having been sent to other projects).

The change to each acre is based entirely on the contents of that acre as well as the number of open, wooded, or lumberyard acres adjacent to it at the start of each minute. Here, "adjacent" means any of the eight acres surrounding that acre. (Acres on the edges of the lumber collection area might have fewer than eight adjacent acres; the missing acres aren't counted.)

In particular:
```
    An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
    An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
    An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
```
These changes happen across all acres simultaneously, each of them using the state of all acres at the beginning of the minute and changing to their new form by the end of that same minute. Changes that happen during the minute don't affect each other.

For example, suppose the lumber collection area is instead only 10 by 10 acres with this initial configuration:
```
Initial state:
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.

After 1 minute:
.......##.
......|###
.|..|...#.
..|#||...#
..##||.|#|
...#||||..
||...|||..
|||||.||.|
||||||||||
....||..|.

After 2 minutes:
.......#..
......|#..
.|.|||....
..##|||..#
..###|||#|
...#|||||.
|||||||||.
||||||||||
||||||||||
.|||||||||

After 3 minutes:
.......#..
....|||#..
.|.||||...
..###|||.#
...##|||#|
.||##|||||
||||||||||
||||||||||
||||||||||
||||||||||

After 4 minutes:
.....|.#..
...||||#..
.|.#||||..
..###||||#
...###||#|
|||##|||||
||||||||||
||||||||||
||||||||||
||||||||||

After 5 minutes:
....|||#..
...||||#..
.|.##||||.
..####|||#
.|.###||#|
|||###||||
||||||||||
||||||||||
||||||||||
||||||||||

After 6 minutes:
...||||#..
...||||#..
.|.###|||.
..#.##|||#
|||#.##|#|
|||###||||
||||#|||||
||||||||||
||||||||||
||||||||||

After 7 minutes:
...||||#..
..||#|##..
.|.####||.
||#..##||#
||##.##|#|
|||####|||
|||###||||
||||||||||
||||||||||
||||||||||

After 8 minutes:
..||||##..
..|#####..
|||#####|.
||#...##|#
||##..###|
||##.###||
|||####|||
||||#|||||
||||||||||
||||||||||

After 9 minutes:
..||###...
.||#####..
||##...##.
||#....###
|##....##|
||##..###|
||######||
|||###||||
||||||||||
||||||||||

After 10 minutes:
.||##.....
||###.....
||##......
|##.....##
|##.....##
|##....##|
||##.####|
||#####|||
||||#|||||
||||||||||
```
After 10 minutes, there are 37 wooded acres and 31 lumberyards. Multiplying the number of wooded acres by the number of lumberyards gives the total resource value after ten minutes: 37 * 31 = 1147.

What will the total resource value of the lumber collection area be after 10 minutes?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
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

for _ in range(10):

    nxt = [row[:] for row in grid]

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
                    lumber >= 1 and
                    trees >= 1
                ):
                    nxt[y][x] = "."

    grid = nxt

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

let grid = fs.readFileSync('input_18', 'utf8')
    .trim()
    .split('\n')
    .map(r => r.split(''));

const H = grid.length;
const W = grid[0].length;

const dirs = [
    [-1,-1], [0,-1], [1,-1],
    [-1, 0],         [1, 0],
    [-1, 1], [0, 1], [1, 1]
];

for (let minute = 0; minute < 10; minute++) {

    const next = grid.map(r => [...r]);

    for (let y = 0; y < H; y++) {
        for (let x = 0; x < W; x++) {

            let trees = 0;
            let lumber = 0;

            for (const [dx, dy] of dirs) {

                const nx = x + dx;
                const ny = y + dy;

                if (
                    nx < 0 || ny < 0 ||
                    nx >= W || ny >= H
                ) continue;

                if (grid[ny][nx] === '|')
                    trees++;

                if (grid[ny][nx] === '#')
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
                if (
                    !(lumber >= 1 &&
                      trees >= 1)
                )
                    next[y][x] = '.';
            }
        }
    }

    grid = next;
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
- This Solves the Part 01 of this challenge.
