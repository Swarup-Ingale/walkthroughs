# URL
https://adventofcode.com/2018/day/6

# Description 
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:
```
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
```
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:
```
..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
```
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:
```
aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
```
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
from collections import defaultdict

coords = []

with open("input_06") as f:
    for line in f:
        x, y = map(int, line.strip().split(", "))
        coords.append((x, y))

min_x = min(x for x, y in coords)
max_x = max(x for x, y in coords)
min_y = min(y for x, y in coords)
max_y = max(y for x, y in coords)

areas = defaultdict(int)
infinite = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):

        distances = [
            abs(x - cx) + abs(y - cy)
            for cx, cy in coords
        ]

        best = min(distances)

        if distances.count(best) > 1:
            continue

        owner = distances.index(best)

        areas[owner] += 1

        if (
            x == min_x or
            x == max_x or
            y == min_y or
            y == max_y
        ):
            infinite.add(owner)

answer = max(
    area
    for idx, area in areas.items()
    if idx not in infinite
)

print(answer)
```
- The Javascript version of the code is as follows:
```
const fs = require('fs');

const coords = fs
    .readFileSync('input_06', 'utf8')
    .trim()
    .split('\n')
    .map(line =>
        line.split(', ').map(Number)
    );

const xs = coords.map(c => c[0]);
const ys = coords.map(c => c[1]);

const minX = Math.min(...xs);
const maxX = Math.max(...xs);
const minY = Math.min(...ys);
const maxY = Math.max(...ys);

const areas = {};
const infinite = new Set();

for (let x = minX; x <= maxX; x++) {
    for (let y = minY; y <= maxY; y++) {

        const distances =
            coords.map(
                ([cx, cy]) =>
                    Math.abs(x - cx) +
                    Math.abs(y - cy)
            );

        const best =
            Math.min(...distances);

        const count =
            distances.filter(
                d => d === best
            ).length;

        if (count > 1)
            continue;

        const owner =
            distances.indexOf(best);

        areas[owner] =
            (areas[owner] || 0) + 1;

        if (
            x === minX ||
            x === maxX ||
            y === minY ||
            y === maxY
        ) {
            infinite.add(owner);
        }
    }
}

let answer = 0;

for (const owner in areas) {
    if (
        !infinite.has(
            Number(owner)
        )
    ) {
        answer = Math.max(
            answer,
            areas[owner]
        );
    }
}

console.log(answer);
```
- This solves the Part 01 of this challenge.
