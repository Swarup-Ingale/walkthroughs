# URL
https://adventofcode.com/2018/day/6#part2

# Description
On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:
```
..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.
```
In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:
```
    Distance to coordinate A: abs(4-1) + abs(3-1) =  5
    Distance to coordinate B: abs(4-1) + abs(3-6) =  6
    Distance to coordinate C: abs(4-8) + abs(3-3) =  4
    Distance to coordinate D: abs(4-3) + abs(3-4) =  2
    Distance to coordinate E: abs(4-5) + abs(3-5) =  3
    Distance to coordinate F: abs(4-8) + abs(3-9) = 10
    Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
```
Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

# Method of Solve 
- The Part 02 of this challenge can be solved using the following code:
- The python version is as follows:
```
coords = []

with open("input_06") as f:
    for line in f:
        x, y = map(int, line.strip().split(", "))
        coords.append((x, y))

min_x = min(x for x, y in coords)
max_x = max(x for x, y in coords)
min_y = min(y for x, y in coords)
max_y = max(y for x, y in coords)

region = 0

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):

        total = sum(
            abs(x - cx) + abs(y - cy)
            for cx, cy in coords
        )

        if total < 10000:
            region += 1

print(region)
```
- The javascript version of code is :
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

let region = 0;

for (let x = minX; x <= maxX; x++) {
    for (let y = minY; y <= maxY; y++) {

        let total = 0;

        for (const [cx, cy] of coords) {
            total +=
                Math.abs(x - cx) +
                Math.abs(y - cy);
        }

        if (total < 10000) {
            region++;
        }
    }
}

console.log(region);
```

# This Solves the Day 06 of The Advent of Code.
