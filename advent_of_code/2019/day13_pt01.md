# URL
https://adventofcode.com/2019/day/13

# Description
As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth, you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care package.

It's a new game for the ship's arcade cabinet! Unfortunately, the arcade is all the way on the other end of the ship. Surely, it won't be hard to build your own - the care package even comes with schematics.

The arcade cabinet runs Intcode software like the game the Elves sent (your puzzle input). It has a primitive screen capable of drawing square tiles on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id. The tile id is interpreted as follows:
```
    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.
```
For example, a sequence of output values like 1,2,3,6,5,4 would draw a horizontal paddle tile (1 tile from the left and 2 tiles from the top) and a ball tile (6 tiles from the left and 5 tiles from the top).

Start the game. How many block tiles are on the screen when the game exits?

# Method of Solve
- The Part 01 of this challenge can be solved as follows:
- The Python Version is as follows:
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
			raise ValueError(f"Invalid write mode: {mode}")

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
				addres = self.write_address(mode3, self.ip + 3)
				self.write(address, a * b)
				self.ip += 4

			elif opcode == 3:
				if not self.inputs:
					self.inputs.append(0)
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

with open("input13", "r") as f:
	program = list(map(int, f.read().strip().split(",")))

computer = Intcode(program)

tiles = {}

while not computer.halted:
	x = computer.run_until_output()
	if x is None:
		break
	y = computer.run_until_output()
	if y is None:
		break

	tile = computer.run_until_output()

	if tile is None:
		break

	tiles[(x, y)] = tile

block_count = sum(
	1
	for tile in tiles.values()
	if tile == 2
)

print(f"Block tiles: {block_count}")
```
- The Javascript version is as follows:
```
const fs = require("fs");


const program = fs
	.readFileSync("input13", "utf-8")
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
			return this.read(
				this.read(index)
			);
		}

		else if (mode === 1) {
			return this.read(index);
		}

		else if (mode === 2) {
			return this.read(
				this.relativeBase + this.read(index)
			);
		}

		else {
			throw new Error(
				`Invalid parameter mode: ${mode}`
			);
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
			throw new Error(
				`Invalid write mode: ${mode}`
			);
		}
	}


	runUntilOutput() {
		while (true) {
			const instruction = this.read(this.ip);

			const opcode = instruction % 100;

			const mode1 =
				Math.floor(instruction / 100) % 10;

			const mode2 =
				Math.floor(instruction / 1000) % 10;

			const mode3 =
				Math.floor(instruction / 10000) % 10;


			if (opcode === 99) {
				this.halted = true;
				return null;
			}


			else if (opcode === 1) {
				const a = this.parameter(
					mode1,
					this.ip + 1
				);

				const b = this.parameter(
					mode2,
					this.ip + 2
				);

				const address = this.writeAddress(
					mode3,
					this.ip + 3
				);

				this.write(
					address,
					a + b
				);

				this.ip += 4;
			}


			else if (opcode === 2) {
				const a = this.parameter(
					mode1,
					this.ip + 1
				);

				const b = this.parameter(
					mode2,
					this.ip + 2
				);

				const address = this.writeAddress(
					mode3,
					this.ip + 3
				);

				this.write(
					address,
					a * b
				);

				this.ip += 4;
			}


			else if (opcode === 3) {
				if (this.inputs.length === 0) {
					throw new Error(
						"Input required but none available."
					);
				}

				const address = this.writeAddress(
					mode1,
					this.ip + 1
				);

				this.write(
					address,
					this.inputs.shift()
				);

				this.ip += 2;
			}


			else if (opcode === 4) {
				const output = this.parameter(
					mode1,
					this.ip + 1
				);

				this.ip += 2;

				return output;
			}


			else if (opcode === 5) {
				const condition = this.parameter(
					mode1,
					this.ip + 1
				);

				if (condition !== 0) {
					this.ip = this.parameter(
						mode2,
						this.ip + 2
					);
				}

				else {
					this.ip += 3;
				}
			}


			else if (opcode === 6) {
				const condition = this.parameter(
					mode1,
					this.ip + 1
				);

				if (condition === 0) {
					this.ip = this.parameter(
						mode2,
						this.ip + 2
					);
				}

				else {
					this.ip += 3;
				}
			}


			else if (opcode === 7) {
				const a = this.parameter(
					mode1,
					this.ip + 1
				);

				const b = this.parameter(
					mode2,
					this.ip + 2
				);

				const address = this.writeAddress(
					mode3,
					this.ip + 3
				);

				this.write(
					address,
					a < b ? 1 : 0
				);

				this.ip += 4;
			}


			else if (opcode === 8) {
				const a = this.parameter(
					mode1,
					this.ip + 1
				);

				const b = this.parameter(
					mode2,
					this.ip + 2
				);

				const address = this.writeAddress(
					mode3,
					this.ip + 3
				);

				this.write(
					address,
					a === b ? 1 : 0
				);

				this.ip += 4;
			}


			else if (opcode === 9) {
				this.relativeBase += this.parameter(
					mode1,
					this.ip + 1
				);

				this.ip += 2;
			}


			else {
				throw new Error(
					`Unknown opcode ${opcode} at position ${this.ip}`
				);
			}
		}
	}
}


const computer = new Intcode(program);


const tiles = new Map();


function tileKey(x, y) {
	return `${x},${y}`;
}


while (!computer.halted) {

	const x = computer.runUntilOutput();

	if (x === null) {
		break;
	}


	const y = computer.runUntilOutput();

	if (y === null) {
		break;
	}


	const tile = computer.runUntilOutput();

	if (tile === null) {
		break;
	}


	tiles.set(
		tileKey(x, y),
		tile
	);
}


let blockCount = 0;

for (const tile of tiles.values()) {
	if (tile === 2) {
		blockCount++;
	}
}


console.log(
	"Block tiles:",
	blockCount
);
```
- This Solves Part 01 of this challenge.
