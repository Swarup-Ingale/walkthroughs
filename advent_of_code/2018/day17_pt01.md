# URL
https://adventofcode.com/2018/day/17

# Description
You arrive in the year 18. If it weren't for the coat you got in 1018, you would be very cold: the North Pole base hasn't even been constructed.

Rather, it hasn't been constructed yet. The Elves are making a little progress, but there's not a lot of liquid water in this climate, so they're getting very dehydrated. Maybe there's more underground?

You scan a two-dimensional vertical slice of the ground nearby and discover that it is mostly sand with veins of clay. The scan only provides data with a granularity of square meters, but it should be good enough to determine how much water is trapped there. In the scan, x represents the distance to the right, and y represents the distance down. There is also a spring of water near the surface at x=500, y=0. The scan identifies which square meters are clay (your puzzle input).

For example, suppose your scan shows the following veins of clay:
```
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
```
Rendering clay as #, sand as ., and the water spring as +, and with x increasing to the right and y increasing downward, this becomes:
```
   44444455555555
   99999900000000
   45678901234567
 0 ......+.......
 1 ............#.
 2 .#..#.......#.
 3 .#..#..#......
 4 .#..#..#......
 5 .#.....#......
 6 .#.....#......
 7 .#######......
 8 ..............
 9 ..............
10 ....#.....#...
11 ....#.....#...
12 ....#.....#...
13 ....#######...
```
The spring of water will produce water forever. Water can move through sand, but is blocked by clay. Water always moves down when possible, and spreads to the left and right otherwise, filling space that has clay on both sides and falling out otherwise.

For example, if five squares of water are created, they will flow downward until they reach the clay and settle there. Water that has come to rest is shown here as ~, while sand through which water has passed (but which is now dry again) is shown as |:
```
......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#....|#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
```
Two squares of water can't occupy the same location. If another five squares of water are created, they will settle on the first five, filling the clay reservoir a little more:
```
......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
```
Water pressure does not apply in this scenario. If another four squares of water are created, they will stay on the right side of the barrier, and no water will reach the left side:
```
......+.......
......|.....#.
.#..#.|.....#.
.#..#~~#......
.#..#~~#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
```
At this point, the top reservoir overflows. While water can reach the tiles above the surface of the water, it cannot settle there, and so the next five squares of water settle like this:
```
......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#...|.#...
....#...|.#...
....#~~~~~#...
....#######...
```
Note especially the leftmost |: the new squares of water can reach this tile, but cannot stop there. Instead, eventually, they all fall to the right and settle in the reservoir below.

After 10 more squares of water, the bottom reservoir is also full:
```
......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#~~~~~#...
....#~~~~~#...
....#~~~~~#...
....#######...
```
Finally, while there is nowhere left for the water to settle, it can reach a few more tiles before overflowing beyond the bottom of the scanned data:
```
......+.......    (line not counted: above minimum y value)
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
...|||||||||..
...|#~~~~~#|..
...|#~~~~~#|..
...|#~~~~~#|..
...|#######|..
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
```
How many tiles can be reached by the water? To prevent counting forever, ignore tiles with a y coordinate smaller than the smallest y coordinate in your scan data or larger than the largest one. Any x coordinate is valid. In this example, the lowest y coordinate given is 1, and the highest is 13, causing the water spring (in row 0) and the water falling off the bottom of the render (in rows 14 through infinity) to be ignored.

So, in the example above, counting both water at rest (~) and other sand tiles the water can hypothetically reach (|), the total number of tiles the water can reach is 57.

How many tiles can the water reach within the range of y values in your scan?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
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
- This Solves the Part 01 of this challenge.
