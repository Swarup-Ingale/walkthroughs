# URL
https://adventofcode.com/2019/day/3

# Description
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:
```
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:
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
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:
```
    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
```
What is the Manhattan distance from the central port to the closest intersection?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input03") as f:
    wire1, wire2 = f.read().strip().splitlines()


def trace(wire):
    x = y = 0
    visited = set()

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
            visited.add((x, y))

    return visited


path1 = trace(wire1)
path2 = trace(wire2)

intersections = path1 & path2

print(min(abs(x) + abs(y) for x, y in intersections))
```
- The Javascript version of code is as follows:
```
const fs = require("fs");

const [wire1, wire2] = fs
	.readFileSync("input03", "utf-8")
	.trim()
	.split("\n");

function trace(wire) {
	let x = 0;
	let y = 0;

	const visited = new Set();

	const dirs = {
		U: [0, 1],
		D: [0, -1],
		L: [-1, 0],
		R: [1, 0],
	};

	for (const move of wire.split(",")) {
		const [dx, dy] = dirs[move[0]];
		const length = Number(move.slice(1));

		for (let i = 0; i < length; i++) {
			x += dx;
			y += dy;
			visited.add(`${x},${y}`);
		}
	}

	return visited;
}

const path1 = trace(wire1);
const path2 = trace(wire2);

let answer = Infinity;

for (const point of path1) {
	if (path2.has(point)) {
		const [x, y] = point.split(",").map(Number);
		answer = Math.min(answer, Math.abs(x) + Math.abs(y));
	}
}

console.log(answer);
```
- This Solves The Part 01 of this challenge.
