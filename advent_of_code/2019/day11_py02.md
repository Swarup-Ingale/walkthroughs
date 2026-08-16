# URL
https://adventofcode.com/2019/day/11#part2

# Description
You're not sure what it's trying to paint, but it's definitely not a registration identifier. The Space Police are getting impatient.

Checking your external ship cameras again, you notice a white panel marked "emergency hull painting robot starting panel". The rest of the panels are still black, but it looks like the robot was expecting to start on a white panel, not a black one.

Based on the Space Law Space Brochure that the Space Police attached to one of your windows, a valid registration identifier is always eight capital letters. After starting the robot on a single white panel instead, what registration identifier does it paint on your hull?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Javascript version is as follows:
```
const fs = require("fs");

const program = fs
	.readFileSync("input11", "utf-8")
	.trim()
	.split(",")
	.map(Number);

class Intcode {
	constructor(program) {
		this.memory = new Map();

		for (let i = 0; i < program.length; i++) {
			this.memory.set(i, program[i]);
		}

		this.ip = 0;
		this.relativeBase = 0;
		this.inputs = [];
		this.halted = false;
	}

	read(address) {
		return this.memory.get(address) ?? 0;
	}

	write(address, value) {
		this.memory.set(address, value);
	}

	parameter(mode, index) {
		if (mode === 0) {
			return this.read(this.read(index));
		}

		else if (mode === 1) {
			return this.read(index);
		}

		else if (mode === 2) {
			return this.read(this.relativeBase + this.read(index));
		}

		else {
			throw new Error(`Invalid Parameter mode: ${mode}`);
		}
	}

	writeAddress(mode, index) {
		if (mode === 0) {
			return this.read(index);
		}

		else if (mode === 2) {
			return this.relativeBase + this.read(index);
		}

		else {
			throw new Error(`Invalid write mode: ${mode}`);
		}
	}

	runUntilOutput() {
		while (true) {
			const instruction = this.read(this.ip);

			const opcode = instruction % 100;

			const mode1 = Math.floor(instruction / 100) % 10;
			const mode2 = Math.floor(instruction / 1000) % 10;
			const mode3 = Math.floor(instruction / 10000) % 10;

			if (opcode === 99) {
				this.halted = true;
				return null;
			}

			else if (opcode === 1) {
				const a = this.parameter(mode1, this.ip + 1);
				const b = this.parameter(mode2, this.ip + 2);

				const address = this.writeAddress(mode3, this.ip + 3);

				this.write(address, a + b);

				this.ip += 4;
			}

			else if (opcode === 2) {
				const a = this.parameter(mode1, this.ip + 1);
				const b = this.parameter(mode2, this.ip + 2);

				const address = this.writeAddress(mode3, this.ip + 3);

				this.write(address, a * b);

				this.ip += 4;
			}

			else if (opcode === 3) {
				if (this.inputs.length === 0) {
					throw new Error("Input required but none available...");
				}

				const address = this.writeAddress(mode1, this.ip + 1);

				this.write(address, this.inputs.shift());

				this.ip += 2;
			}

			else if (opcode === 4) {
				const output = this.parameter(mode1, this.ip + 1);

				this.ip += 2;

				return output;
			}

			else if (opcode === 5) {
				const condition = this.parameter(mode1, this.ip + 1);

				if (condition !== 0) {
					this.ip = this.parameter(mode2, this.ip + 2);
				}

				else {
					this.ip += 3;
				}
			}

			else if (opcode === 6) {
				const condition = this.parameter(mode1, this.ip + 1);

				if (condition === 0) {
					this.ip = this.parameter(mode2, this.ip + 2);
				}

				else {
					this.ip += 3;
				}
			}

			else if (opcode === 7) {
				const a = this.parameter(mode1, this.ip + 1);
				const b = this.parameter(mode2, this.ip + 2);

				const address = this.writeAddress(mode3, this.ip + 3);

				this.write(address, a < b ? 1 : 0);

				this.ip += 4;
			}

			else if (opcode === 8) {
				const a = this.parameter(mode1, this.ip + 1);
				const b = this.parameter(mode2, this.ip + 2);

				const address = this.writeAddress(mode3, this.ip + 3);

				this.write(address, a === b ? 1 : 0);

				this.ip += 4;
			}

			else if (opcode === 9) {
				this.relativeBase += this.parameter(mode1, this.ip + 1);

				this.ip += 2;
			}

			else {
				throw new Error(`Unknown opcode ${opcode} at position ${this.ip}`);
			}
		}
	}
}

const computer = new Intcode(program);

const panels = new Map();
panels.set("0, 0", 1);

const painted = new Set();

let x = 0;
let y = 0;
let direction = 0;

let dx = [0, 1, 0, -1];
let dy = [1, 0, -1 ,0];

function panelKey(x, y) {
	return `${x}, ${y}`;
}

while (!computer.halted) {
	const key = panelKey(x, y);

	const currentColor = panels.get(key) ?? 0;

	computer.inputs.push(currentColor);

	const paint = computer.runUntilOutput();

	if (paint === null) {
		break;
	}

	panels.set(key, paint);
	painted.add(key);

	const turn = computer.runUntilOutput();

	if (turn === null) {
		break;
	}

	if (turn === 0) {
		direction = (direction - 1 + 4) % 4;
	}

	else if (turn === 1) {
		direction = (direction + 1) % 4;
	}

	else {
		throw new Error(`Invalid turn instruction: ${turn}`);
	}

	x += dx[direction];
	y += dy[direction];
}

console.log("Registration Identifier: ");


if (panels.size > 0) {
	const coordinates = [
		...panels.keys()
	].map(key => key.split(",").map(Number));


	const xs = coordinates.map(
		([x, y]) => x
	);

	const ys = coordinates.map(
		([x, y]) => y
	);


	const minX = Math.min(...xs);
	const maxX = Math.max(...xs);

	const minY = Math.min(...ys);
	const maxY = Math.max(...ys);


	for (let y = maxY; y >= minY; y--) {
		let line = "";

		for (let x = minX; x <= maxX; x++) {
			const key = panelKey(x, y);

			if ((panels.get(key) ?? 0) === 1) {
				line += "█";
			}

			else {
				line += " ";
			}
		}

		console.log(line);
	}
}
```
- The Python version is as follows:
```
from collections import defaultdict, deque

class Intcode:
	def __init__(self, program):
		self.memory = defaultdict(int)

		for i, value in enumerate(program):
			self.memory[i] = value

		self.ip = 0
		self.relative_base = 0

		self.inputs = deque()

		self.halted = False

	def read(self, address):
		return self.memory[address]

	def write(self, address, value):
		self.memory[address] = value

	def parameter(self, mode, index):
		if mode == 0:
			return self.read(self.read(index))

		elif mode == 1:
			return self.read(index)

		elif mode == 2:
			return self.read(self.relative_base + self.read(index))

		else:
			raise ValueError(f"Invalid parameter mode: {mode}")

	def write_address(self, mode, index):
		if mode == 0:
			return self.read(index)

		elif mode == 2:
			return self.relative_base + self.read(index)

		else:
			raise ValueError(f"Invalid write Mode: {mode}")

	def run_until_output(self):
		while True:
			instruction = self.read(self.ip)

			opcode = instruction % 100

			mode1 = (instruction // 100) % 10
			mode2 = (instruction // 1000) % 10
			mode3 = (instruction // 10000) % 10

			if opcode == 99:
				self.halted = True
				return None

			elif opcode == 1:
				a = self.parameter(mode1, self.ip + 1)
				b = self.parameter(mode2, self.ip + 2)

				address = self.write_address(mode3, self.ip + 3)

				self.write(address, a + b)

				self.ip += 4

			elif opcode == 2:
				a = self.parameter(mode1, self.ip + 1)
				b = self.parameter(mode2, self.ip + 2)

				address = self.write_address(mode3, self.ip + 3)

				self.write(address, a * b)

				self.ip += 4

			elif opcode == 3:
				if not self.inputs:
					raise RuntimeError("Input Required but none available")

				address = self.write_address(mode1, self.ip + 1)

				self.write(address, self.inputs.popleft())

				self.ip += 2

			elif opcode == 4:
				output = self.parameter(mode1, self.ip + 1)

				self.ip += 2
				return output

			elif opcode == 5:
				condition = self.parameter(mode1, self.ip + 1)

				if condition != 0:
					self.ip = self.parameter(mode2, self.ip + 2)

				else:
					self.ip += 3

			elif opcode == 6:
				condition = self.parameter(mode1, self.ip + 1)

				if condition == 0:
					self.ip = self.parameter(mode2, self.ip + 2)

				else:
					self.ip += 3

			elif opcode == 7:
				a = self.parameter(mode1, self.ip + 1)
				b = self.parameter(mode2, self.ip + 2)

				address = self.write_address(mode3, self.ip + 3)

				self.write(address, 1 if a < b else 0)

				self.ip += 4

			elif opcode == 8:
				a = self.parameter(mode1, self.ip + 1)
				b = self.parameter(mode2, self.ip + 2)

				address = self.write_address(mode3, self.ip + 3)

				self.write(address, 1 if a == b else 0)

				self.ip += 4

			elif opcode == 9:
				self.relative_base += self.parameter(mode1, self.ip + 1)

				self.ip += 2

			else:
				raise ValueError(f"Unknown opcode {opcode} at position {self.ip}")

with open("input11", "r") as f:
	program = list(map(int, f.read().strip().split(",")))

computer = Intcode(program)

panels = defaultdict(int)
panels[(0, 0)] = 1

painted = set()

x = 0
y = 0

direction = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while not computer.halted:
	current_color = panels[(x, y)]

	computer.inputs.append(current_color)

	paint = computer.run_until_output()

	if paint is None:
		break

	panels[(x, y)] = paint
	painted.add((x, y))

	turn = computer.run_until_output()

	if turn is None:
		break

	if turn == 0:
		direction = (direction - 1) % 4

	elif turn == 1:
		direction = (direction + 1) % 4

	else:
		raise ValueError(f"Invalid turn instruction: {turn}")

	x += dx[direction]
	y += dy[direction]

print("Registration Identifier: ");

if panels:
	min_x = min(x for x, y in panels)
	max_x = max(x for x, y in panels)

	min_y = min(y for x, y in panels)
	max_y = max(y for x, y in panels)

	for y in range(max_y, min_y - 1, -1):
		line = ""

		for x in range(min_x, max_x + 1):
			if panels[(x, y)] == 1:
				line += "█"

			else:
				line += " "

		print(line)
```

# This Concludes Day 11 of The Advent of Code.
