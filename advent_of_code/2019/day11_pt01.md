# URL
https://adventofcode.com/2019/day/11

# Description
On the way to Jupiter, you're pulled over by the Space Police.

"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible registration identifier! You have 24 hours to comply or be sent to Space Jail!"

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three hours for their reply signal to reach you, they send instructions for how to power up the emergency hull painting robot and even provide a small Intcode program (your puzzle input) that will cause it to paint your ship appropriately.

There's just one problem: you don't have an emergency hull painting robot.

You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of square panels on the side of your ship, detect the color of its current panel, and paint its current panel black or white. (All of the panels are currently black.)

The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will output two values:
```
    First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
    Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
```
After the robot turns, it should always move forward exactly one panel. The robot starts facing up.

The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the Intcode computer inside the robot during this process.

For example, suppose the robot is about to start running. Drawing black panels as ., white panels as #, and the robot pointing the direction it is facing (< ^ > v), the initial state and region near the robot looks like this:
```
.....
.....
..^..
.....
.....
```
The panel under the robot (not visible here because a ^ is shown instead) is also black, and so any input instructions at this point should be provided 0. Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left). After taking these actions and moving forward one panel, the region now looks like this:
```
.....
.....
.<#..
.....
.....
```
Input instructions should still be provided 0. Next, the robot might output 0 (paint black) and then 0 (turn left):
```
.....
.....
..#..
.v...
.....
```
After more outputs (1,0, 1,0):
```
.....
.....
..^..
.##..
.....
```
The robot is now back where it started, but because it is now on a white panel, input instructions should be provided 1. After several more outputs (0,1, 1,0, 1,0), the area looks like this:
```
.....
..<#.
...#.
.##..
.....
```
Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to know the number of panels it paints at least once, regardless of color. In the example above, the robot painted 6 panels at least once. (It painted its starting panel twice, but that panel is still only counted once; it also never painted the panel it ended on.)

Build a new emergency hull painting robot and run the Intcode program on it. How many panels does it paint at least once?

# Method of Solve
- The Part 01 of this challenge can be solved as follows:
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

console.log(`Panels Painted are : ${painted.size}`);
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

print(f"Painted Panels are: {len(painted)}")
```
- This Solves the Part 01 of this challenge.
