# URL
https://adventofcode.com/2019/day/10

# Description
You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.

The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).

The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).

Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.

For example, consider the following map:
```
.#..#
.....
#####
....#
...##
```
The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:
```
.7..7
.....
67775
....7
...87
```
Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:
```
#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c
```
Here are some larger examples:

    Best is 5,8 with 33 other asteroids detected:
```
    ......#.#.
    #..#.#....
    ..#######.
    .#.#.###..
    .#..#.....
    ..#....#.#
    #..#....#.
    .##.#..###
    ##...#..#.
    .#....####
```
    Best is 1,2 with 35 other asteroids detected:
```
    #.#...#.#.
    .###....#.
    .#....#...
    ##.#.#.#.#
    ....#.#.#.
    .##..###.#
    ..#...##..
    ..##....##
    ......#...
    .####.###.
```
    Best is 6,3 with 41 other asteroids detected:
```
    .#..#..###
    ####.###.#
    ....###.#.
    ..###.##.#
    ##.##.#.#.
    ....###..#
    ..#.#..#.#
    #..#.#.###
    .##...##.#
    .....#.#..
```
    Best is 11,13 with 210 other asteroids detected:
```
    .#..##.###...#######
    ##.############..##.
    .#.######.########.#
    .###.#######.####.#.
    #####.##.#.##.###.##
    ..#####..#.#########
    ####################
    #.####....###.#.#.##
    ##.#################
    #####.##.###..####..
    ..######..##.#######
    ####.##.####...##..#
    .#####..#.######.###
    ##...#.##########...
    #.##########.#######
    .####.#.###.###.#.##
    ....##.##.###..#####
    .#.#.###########.###
    #.#.#.#####.####.###
    ###.##.####.##.#..##
```
Find the best location for a new monitoring station. How many other asteroids can be detected from that location?

# Method of Solve
- The Part 01 of this challenge can be solved as follows:
- The Javascript version is as follows:
```
const fs = require("fs");

const grid = fs
	.readFileSync("input10", "utf-8")
	.trim()
	.split("\n");

const asteroids = [];

for (let y = 0; y < grid.length; y++) {
	for (let x = 0; x < grid[y].length; x++) {
		if (grid[y][x] === "#") {
			asteroids.push([x, y]);
		}
	}
}

function gcd(a, b) {
	while (b !== 0) {
		const temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}

function visibleFrom(x1, y1) {
	const directions = new Set();

	for (const [x2, y2] of asteroids) {
		if (x1 === x2 && y1 === y2) {
			continue;
		}

		let dx = x2 - x1;
		let dy = y2 - y1;

		const divisor = gcd(Math.abs(dx), Math.abs(dy));

		dx /= divisor;
		dy /= divisor;

		directions.add(`${dx}, ${dy}`);
	}

	return directions.size;
}

let best = null;
let bestCount = 0;

for (const [x, y] of asteroids) {
	const count = visibleFrom(x, y);

	if (count > bestCount) {
		bestCount = count;
		best = [x, y];
	}
}

console.log(`Best Location is: ${best}`);
console.log(`Visible Asteroids are: ${bestCount}`);
```
- The Python version is as follows:
```
from math import gcd

with open("input10", "r") as f:
	grid = f.read().strip().splitlines()

asteroids = []

for y, row in enumerate(grid):
	for x, value in enumerate(row):
		if value == "#":
			asteroids.append((x, y))

def visible_from(x1, y1):
	directions = set()

	for x2, y2 in asteroids:
		if (x1, y1) == (x2, y2):
			continue

		dx = x2 - x1
		dy = y2 - y1

		divisor = gcd(abs(dx), abs(dy))

		dx //= divisor
		dy //= divisor

		directions.add((dx, dy))

	return len(directions)

best = None
best_count = 0

for x, y in asteroids:
	count = visible_from(x, y)

	if count > best_count:
		best_count = count
		best = (x, y)

print("Best Location:", best)
print("Visible Asteroids:", best_count)
```
- This Solves the part 01 of this challenge.
