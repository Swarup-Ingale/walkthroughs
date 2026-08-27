# URL
https://adventofcode.com/2019/day/13#part2

# Description
The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.

The arcade cabinet has a joystick that can move left and right. The software reads the position of the joystick with input instructions:
```
    If the joystick is in the neutral position, provide 0.
    If the joystick is tilted to the left, provide -1.
    If the joystick is tilted to the right, provide 1.
```
The arcade cabinet also has a segment display capable of showing a single number that represents the player's current score. When three output instructions specify X=-1, Y=0, the third output instruction is not a tile; the value instead specifies the new score to show in the segment display. For example, a sequence of output values like -1,0,12345 would show 12345 as the player's current score.

Beat the game by breaking all the blocks. What is your score after the last block is broken?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Javascript version is as follows:
```
const fs = require("fs");

const program = fs
	.readFileSync("input13", "utf-8")
	.trim()
	.split(",")
	.map(Number);

program[0] = 2;

class Intcode {
	constructor(program) {
		this.memory = new Map();

		for (let i = 0; i < program.length; i++) {
			this.memory.set(i, program[i]);
		}

		this.ip = 0;
		this.relativeBase = 0;
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

		throw new Error(
			`Invalid parameter mode: ${mode}`
		);
	}

	writeAddress(mode, index) {
		if (mode === 0) {
			return this.read(index);
		}

		else if (mode === 2) {
			return this.relativeBase + this.read(index);
		}

		throw new Error(
			`Invalid write mode: ${mode}`
		);
	}

	runUntilEvent(input = null) {
		while (true) {
			const instruction = this.read(this.ip);

			const opcode = instruction % 100;
			const mode1 = Math.floor(instruction / 100) % 10;
			const mode2 = Math.floor(instruction / 1000) % 10;
			const mode3 = Math.floor(instruction / 10000) % 10;

			if (opcode === 99) {
				this.halted = true;

				return {
					type: "halt"
				};
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
				if (input === null) {
					return {
						type: "input"
					};
				}

				const address = this.writeAddress(
					mode1,
					this.ip + 1
				);

				this.write(
					address,
					input
				);

				this.ip += 2;

				input = null;
			}

			else if (opcode === 4) {
				const output = this.parameter(
					mode1,
					this.ip + 1
				);

				this.ip += 2;

				return {
					type: "output",
					value: output
				};
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
					`Unknown Opcode ${opcode} at position ${this.ip}`
				);
			}
		}
	}
}


const computer = new Intcode(program);

const tiles = new Map();

let score = 0;

let ballX = 0;
let paddleX = 0;

let outputs = [];


function tileKey(x, y) {
	return `${x},${y}`;
}


while (!computer.halted) {

	const event = computer.runUntilEvent();


	if (event.type === "halt") {
		break;
	}


	else if (event.type === "input") {

		let joystick = 0;

		if (ballX < paddleX) {
			joystick = -1;
		}

		else if (ballX > paddleX) {
			joystick = 1;
		}

		const inputEvent = computer.runUntilEvent(
			joystick
		);

		if (inputEvent.type === "halt") {
			break;
		}

		if (inputEvent.type === "output") {
			outputs.push(inputEvent.value);
		}
	}


	else if (event.type === "output") {
		outputs.push(event.value);
	}


	if (outputs.length === 3) {

		const x = outputs[0];
		const y = outputs[1];
		const value = outputs[2];

		outputs = [];


		if (x === -1 && y === 0) {
			score = value;
		}

		else {
			tiles.set(
				tileKey(x, y),
				value
			);


			if (value === 3) {
				paddleX = x;
			}

			else if (value === 4) {
				ballX = x;
			}
		}
	}
}


console.log(`Final Score: ${score}`);
```
- The Python version is as follows:
```
from collections import defaultdict


with open("input13", "r") as f:
	program = list(
		map(
			int,
			f.read().strip().split(",")
		)
	)


program[0] = 2


class Intcode:

	def __init__(self, program):
		self.memory = defaultdict(int)

		for i, value in enumerate(program):
			self.memory[i] = value

		self.ip = 0
		self.relative_base = 0
		self.halted = False


	def read(self, address):
		return self.memory[address]


	def write(self, address, value):
		self.memory[address] = value


	def parameter(self, mode, index):

		if mode == 0:
			return self.read(
				self.read(index)
			)

		elif mode == 1:
			return self.read(index)

		elif mode == 2:
			return self.read(
				self.relative_base + self.read(index)
			)

		raise ValueError(
			f"Invalid parameter mode: {mode}"
		)


	def write_address(self, mode, index):

		if mode == 0:
			return self.read(index)

		elif mode == 2:
			return self.relative_base + self.read(index)

		raise ValueError(
			f"Invalid write mode: {mode}"
		)


	def run_until_event(self, input_value=None):

		while True:

			instruction = self.read(self.ip)

			opcode = instruction % 100

			mode1 = (instruction // 100) % 10
			mode2 = (instruction // 1000) % 10
			mode3 = (instruction // 10000) % 10


			if opcode == 99:

				self.halted = True

				return {
					"type": "halt"
				}


			elif opcode == 1:

				a = self.parameter(
					mode1,
					self.ip + 1
				)

				b = self.parameter(
					mode2,
					self.ip + 2
				)

				address = self.write_address(
					mode3,
					self.ip + 3
				)

				self.write(
					address,
					a + b
				)

				self.ip += 4


			elif opcode == 2:

				a = self.parameter(
					mode1,
					self.ip + 1
				)

				b = self.parameter(
					mode2,
					self.ip + 2
				)

				address = self.write_address(
					mode3,
					self.ip + 3
				)

				self.write(
					address,
					a * b
				)

				self.ip += 4


			elif opcode == 3:

				if input_value is None:

					return {
						"type": "input"
					}

				address = self.write_address(
					mode1,
					self.ip + 1
				)

				self.write(
					address,
					input_value
				)

				self.ip += 2

				input_value = None


			elif opcode == 4:

				output = self.parameter(
					mode1,
					self.ip + 1
				)

				self.ip += 2

				return {
					"type": "output",
					"value": output
				}


			elif opcode == 5:

				condition = self.parameter(
					mode1,
					self.ip + 1
				)

				if condition != 0:

					self.ip = self.parameter(
						mode2,
						self.ip + 2
					)

				else:

					self.ip += 3


			elif opcode == 6:

				condition = self.parameter(
					mode1,
					self.ip + 1
				)

				if condition == 0:

					self.ip = self.parameter(
						mode2,
						self.ip + 2
					)

				else:

					self.ip += 3


			elif opcode == 7:

				a = self.parameter(
					mode1,
					self.ip + 1
				)

				b = self.parameter(
					mode2,
					self.ip + 2
				)

				address = self.write_address(
					mode3,
					self.ip + 3
				)

				self.write(
					address,
					1 if a < b else 0
				)

				self.ip += 4


			elif opcode == 8:

				a = self.parameter(
					mode1,
					self.ip + 1
				)

				b = self.parameter(
					mode2,
					self.ip + 2
				)

				address = self.write_address(
					mode3,
					self.ip + 3
				)

				self.write(
					address,
					1 if a == b else 0
				)

				self.ip += 4


			elif opcode == 9:

				self.relative_base += self.parameter(
					mode1,
					self.ip + 1
				)

				self.ip += 2


			else:

				raise ValueError(
					f"Unknown Opcode {opcode} at position {self.ip}"
				)


computer = Intcode(program)


tiles = {}

score = 0

ball_x = 0
paddle_x = 0

outputs = []


def tile_key(x, y):
	return f"{x},{y}"


while not computer.halted:

	event = computer.run_until_event()


	if event["type"] == "halt":
		break


	elif event["type"] == "input":

		joystick = 0

		if ball_x < paddle_x:
			joystick = -1

		elif ball_x > paddle_x:
			joystick = 1


		input_event = computer.run_until_event(
			joystick
		)


		if input_event["type"] == "halt":
			break


		if input_event["type"] == "output":
			outputs.append(
				input_event["value"]
			)


	elif event["type"] == "output":

		outputs.append(
			event["value"]
		)


	if len(outputs) == 3:

		x = outputs[0]
		y = outputs[1]
		value = outputs[2]

		outputs = []


		if x == -1 and y == 0:

			score = value


		else:

			tiles[
				tile_key(x, y)
			] = value


			if value == 3:

				paddle_x = x

			elif value == 4:

				ball_x = x


print(f"Final Score: {score}")
```

# This Concludes Day 13 of The Advent of Code.
