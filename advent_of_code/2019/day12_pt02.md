# URL
https://adventofcode.com/2019/day/12#part2

# Description
All this drifting around in space makes you wonder about the nature of the universe. Does history really repeat itself? You're curious whether the moons will ever return to a previous state.

Determine the number of steps that must occur before all of the moons' positions and velocities exactly match a previous point in time.

For example, the first example above takes 2772 steps before they exactly match a previous point in time; it eventually returns to the initial state:
```
After 0 steps:
pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>
pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>
pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>
pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>

After 2770 steps:
pos=<x=  2, y= -1, z=  1>, vel=<x= -3, y=  2, z=  2>
pos=<x=  3, y= -7, z= -4>, vel=<x=  2, y= -5, z= -6>
pos=<x=  1, y= -7, z=  5>, vel=<x=  0, y= -3, z=  6>
pos=<x=  2, y=  2, z=  0>, vel=<x=  1, y=  6, z= -2>

After 2771 steps:
pos=<x= -1, y=  0, z=  2>, vel=<x= -3, y=  1, z=  1>
pos=<x=  2, y=-10, z= -7>, vel=<x= -1, y= -3, z= -3>
pos=<x=  4, y= -8, z=  8>, vel=<x=  3, y= -1, z=  3>
pos=<x=  3, y=  5, z= -1>, vel=<x=  1, y=  3, z= -1>

After 2772 steps:
pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>
pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>
pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>
pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>
```
Of course, the universe might last for a very long time before repeating. Here's a copy of the second example from above:
```
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
```
This set of initial positions takes 4686774924 steps before it repeats a previous state! Clearly, you might need to find a more efficient way to simulate the universe.

How many steps does it take to reach the first state that exactly matches a previous state?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Python version is as follows:
```
import re
from math import gcd

with open("input12", "r") as f:
	lines = f.read().strip().splitlines()

positions = []

for line in lines:
	positions.append(list(map(int, re.findall(r"-?\d+", line))))

def lcm(a, b):
	return abs(a * b) // gcd(a, b)

def find_cycle(axis):
	pos = [moon[axis] for moon in positions]

	initial_pos = pos[:]

	vel = [0] * len(pos)

	initial_vel = vel[:]

	steps = 0

	while True:
		for i in range(len(pos)):
			for j in range(i + 1, len(pos)):
				if pos[i] < pos[j]:
					vel[i] += 1
					vel[j] -= 1

				elif pos[i] > pos[j]:
					vel[i] -= 1
					vel[j] += 1

		for i in range(len(pos)):
			pos[i] += vel[i]

		steps += 1

		if pos == initial_pos and vel == initial_vel:
			return steps

x_cycle = find_cycle(0)
y_cycle = find_cycle(1)
z_cycle = find_cycle(2)

print(f"X Cycle : {x_cycle}")
print(f"Y Cycle : {y_cycle}")
print(f"Z Cycle : {z_cycle}")

answer = lcm(lcm(x_cycle, y_cycle), z_cycle)

print(f"System Cycle: {answer}")
```
- The Javascript version is :
```
const fs = require("fs");

const lines = fs
	.readFileSync("input12", "utf-8")
	.trim()
	.split("\n");

const positions = [];

for (const line of lines) {
	const values = line.match(/-?\d+/g).map(Number);
	positions.push(values);
}

function gcd(a, b) {
	while (b !== 0) {
		const temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}

function lcm(a, b) {
	return Math.abs(a * b) / gcd(a, b);
}

function findCycle(axis) {
	const pos = positions.map(moon => moon[axis]);

	const initialPos = [...pos];
	const vel = Array(pos.length).fill(0);
	const initialVel = [...vel];
	let steps = 0;

	while (true) {
		for (let i = 0; i < pos.length; i++) {
			for (let j = i + 1; pos.length; j++) {
				if (pos[i] < pos[j]) {
					vel[i] += 1;
					vel[j] -= 1;
				}

				else if (pos[i] > pos[j]) {
					vel[i] -= 1;
					vel[j] += 1;
				}
			}
		}

		for (let i = 0; i < pos.length; i++) {
			pos[i] += vel[i];
		}

		steps++;

		let same = true;

		for (let i = 0; i < pos.length; i++) {
			if (pos[i] !== initialPos[i] || vel[i] !== initialVel[i]) {
				same = false;
				break;
			}
		}

		if (same) {
			return steps;
		}
	}
}

const xCycle = findCycle(0);
const yCycle = findCycle(1);
const zCycle = findCycle(2);

console.log(`X Cycle: ${xCycle}`);
console.log(`Y Cycle: ${yCycle}`);
console.log(`Z Cycle: ${zCycle}`);

const answer = lcm(lcm(xCycle, yCycle), zCycle);

console.log(`System Cycle: ${answer}`);
```

# This Solves Day 12 of The Advent of Code.
