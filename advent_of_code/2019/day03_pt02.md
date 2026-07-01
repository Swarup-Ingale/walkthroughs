# URL
https://adventofcode.com/2019/day/3#part2

# Description
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:
```
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:
```
    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
```
What is the fewest combined steps the wires must take to reach an intersection?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input03", "r") as f:
	wire1, wire2 = f.read().strip().splitlines()

def trace(wire):
	x = y = 0
	steps = 0

	visited = {}

	directions = {
		"U": (0, 1),
		"D": (0, -1),
		"L": (-1, 0),
		"R": (1, 0),
	}

	for move in wire.split(","):
		dx, dy = directions[move[0]]
		length = int(move[1:])

		for _ in range(length):
			x += dx
			y += dy
			steps += 1

			if (x, y) not in visited:
				visited[(x, y)] = steps

	return visited

path1 = trace(wire1)
path2 = trace(wire2)

intersections = path1.keys() & path2.keys()

print(min(path1[p] + path2[p] for p in intersections))
```
- The Javascript version is as follows:
```
const fs = require("fs");

const [wire1, wire2] = fs
	.readFileSync("input03", "utf-8")
	.trim()
	.split("\n");

function trace(wire) {
	let x = 0;
	let y = 0;
	let steps = 0;

	const visited = new Map();

	const dirs = {
		"U": [0, 1],
		"D": [0, -1],
		"L": [-1, 0],
		"R": [1, 0],
	};

	for (const move of wire.split(",")) {
		const [dx, dy] = dirs[move[0]];
		const length = Number(move.slice(1));

		for (let i = 0; i < length; i++) {
			x += dx;
			y += dy;
			steps ++;

			const key = `${x}, ${y}`;

			if (!visited.has(key)) {
				visited.set(key, steps);
			}
		}
	}

	return visited;
}

const path1 = trace(wire1);
const path2 = trace(wire2);

let answer = Infinity;

for (const [point, steps1] of path1) {
	if (path2.has(point)) {
		answer = Math.min(answer, steps1 + path2.get(point));
	}
}

console.log(answer);
```

# This Concludes Day 03 of The Advent of Code.
