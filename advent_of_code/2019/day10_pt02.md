# URL
https://adventofcode.com/2019/day/10#part2

# Description
Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover the worst: there are simply too many asteroids.

The only solution is complete vaporization by giant laser.

Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.

If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation. In other words, the same asteroids that can be detected can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.

For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked X:
```
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
```
The first nine asteroids to get vaporized, in order, would be:
```
.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##
```
Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7) won't have a chance to be vaporized until the next full rotation. The laser continues rotating; the next nine to be vaporized are:
```
.#....###.....#..
##...##...#.....#
##...#......1234.
..#.....X...5##..
..#.9.....8....76
```
The next nine to be vaporized are then:
```
.8....###.....#..
56...9#...#.....#
34...7...........
..2.....X....##..
..1..............
```
Finally, the laser completes its first full rotation (1 through 3), a second rotation (4 through 8), and vaporizes the last asteroid (9) partway through its third rotation:
```
......234.....6..
......1...5.....7
.................
........X....89..
.................
```
In the large example above (the one with the best monitoring station location at 11,13):

- The 1st asteroid to be vaporized is at 11,12.
- The 2nd asteroid to be vaporized is at 12,1.
- The 3rd asteroid to be vaporized is at 12,2.
- The 10th asteroid to be vaporized is at 12,8.
- The 20th asteroid to be vaporized is at 16,0.
- The 50th asteroid to be vaporized is at 16,9.
- The 100th asteroid to be vaporized is at 10,16.
- The 199th asteroid to be vaporized is at 9,6.
- The 200th asteroid to be vaporized is at 8,2.
- The 201st asteroid to be vaporized is at 10,9.-
- The 299th and final asteroid to be vaporized is at 11,1.

The Elves are placing bets on which will be the 200th asteroid to be vaporized. Win the bet by determining which asteroid that will be; what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? (For example, 8,2 becomes 802.)

# Method of Solve
- The Part 02 of this challenge can be solved using the following code
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

		const divisor = gcd(
			Math.abs(dx),
			Math.abs(dy)
		);

		dx /= divisor;
		dy /= divisor;

		directions.add(`${dx},${dy}`);
	}

	return directions.size;
}

let station = null;
let bestCount = 0;

for (const [x, y] of asteroids) {
	const count = visibleFrom(x, y);

	if (count > bestCount) {
		bestCount = count;
		station = [x, y];
	}
}


console.log("Station:", station);
console.log("Visible:", bestCount);

const [sx, sy] = station;

const groups = new Map();

for (const [x, y] of asteroids) {
	if (x === sx && y === sy) {
		continue;
	}

	let dx = x - sx;
	let dy = y - sy;

	const divisor = gcd(
		Math.abs(dx),
		Math.abs(dy)
	);

	const normalizedX = dx / divisor;
	const normalizedY = dy / divisor;

	const key = `${normalizedX},${normalizedY}`;

	const distance =
		dx * dx + dy * dy;

	if (!groups.has(key)) {
		groups.set(key, {
			dx: normalizedX,
			dy: normalizedY,
			asteroids: []
		});
	}

	groups.get(key).asteroids.push({
		distance,
		x,
		y
	});
}

for (const group of groups.values()) {
	group.asteroids.sort(
		(a, b) => a.distance - b.distance
	);
}

const directions = [];

for (const group of groups.values()) {
	let angle = Math.atan2(
		group.dx,
		-group.dy
	);

	if (angle < 0) {
		angle += 2 * Math.PI;
	}

	directions.push({
		angle,
		group
	});
}

directions.sort(
	(a, b) => a.angle - b.angle
);

const vaporized = [];

while (true) {
	let vaporizedThisRound = 0;

	for (const direction of directions) {
		const group = direction.group;

		if (group.asteroids.length === 0) {
			continue;
		}

		const asteroid = group.asteroids.shift();

		vaporized.push([
			asteroid.x,
			asteroid.y
		]);

		vaporizedThisRound++;

		if (vaporized.length === 200) {
			const [x, y] = vaporized[199];

			console.log(
				"200th Asteroid is at:",
				`${x},${y}`
			);

			console.log(
				"Answer:",
				x * 100 + y
			);

			process.exit(0);
		}
	}

	if (vaporizedThisRound === 0) {
		break;
	}
}


throw new Error(
	"Fewer than 200 asteroids were vaporized."
);
```
- The Python version is as follows:
```
from math import gcd, atan2, pi

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

station = None
best_count = 0

for x, y in asteroids:
	count = visible_from(x, y)

	if count > best_count:
		best_count = count
		station = (x, y)

print("Station:", station)
print("Visible:", best_count)

sx, sy = station

groups = {}

for x, y in asteroids:
	if (x, y) == station:
		continue

	dx = x - sx
	dy = y - sy

	angle = atan2(dx, -dy) % (2 * pi)

	distance = dx * dx + dy * dy

	if angle not in groups:
		groups[angle] = []

	groups[angle].append((distance, x, y))


for angle in groups:
	groups[angle].sort()

angles = sorted(groups.keys())

vaporized = []

while groups:
	for angle in angles:
		if angle not in groups:
			continue

		distance, x, y = groups[angle].pop(0)

		vaporized.append((x, y))

		if not groups[angle]:
			del groups[angle]

	angles = sorted(groups.keys())

if len(vaporized) < 200:
	raise ValueError(f"Only {len(vaporized)} asteroids were vaporized.")

x, y = vaporized[199]
print("200th Asteroid is:", (x, y))
print("Answer:", x * 100 + y)
```

# This Concludes Day 10 of The Advent of Code.
