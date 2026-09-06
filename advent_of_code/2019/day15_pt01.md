# URL
https://adventofcode.com/2019/day/15/answer

# Description
Description not found.

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```python
from collections import defaultdict, deque

with open("input15", "r") as f:
	program = list(map(int, f.read().strip().split(",")))

class Intcode:
	def __init__(self, program):
		self.memory = defaultdict(int)

		for i, value in enumerate(program):
			self.memory[i] = value

		self.ip = 0
		self.relative_base = 0
		self.halted = False

	def copy(self):
		computer = Intcode([])

		computer.memory = self.memory.copy()
		computer.ip = self.ip
		computer.relative_base = self.relative_base
		computer.halted = self.halted

		return computer

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

		raise ValueError(f"Invalid parameter mode: {mode}")

	def write_address(self, mode, index):
		if mode == 0:
			return self.read(index)

		elif mode == 2:
			return self.relative_base + self.read(index)

		raise ValueError(f"Invalid write mode: {mode}")

	def run(self, input_value):
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
				address = self.write_address(mode3,self.ip + 3)
				self.write(address, a * b)
				self.ip += 4

			elif opcode == 3:
				address = self.write_address(mode1, self.ip + 1)
				self.write(address, input_value)
				self.ip += 2

			elif opcode == 4:
				output = self.parameter(mode1, self.ip + 1)
				self.ip += 2
				return output

			elif opcode == 5:
				if self.parameter(mode1, self.ip + 1) != 0:
					self.ip = self.parameter(mode2,self.ip + 2)
				else:
					self.ip += 3

			elif opcode == 6:
				if self.parameter(mode1, self.ip + 1) == 0:
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

directions = {
	1: (0, -1),
	2: (0, 1),
	3: (-1, 0),
	4: (1, 0)
}

computer = Intcode(program)

queue = deque()
queue.append((0, 0, computer, 0))

visited = set()
visited.add((0, 0))

while queue:
	x, y, computer, distance = queue.popleft()
	for command, (dx, dy) in directions.items():
		new_x = x + dx
		new_y = y + dy

		if (new_x, new_y) in visited:
			continue

		next_computer = computer.copy()
		status = next_computer.run(command)

		if status == 0:
			continue

		elif status == 1:
			visited.add((new_x, new_y))
			queue.append((new_x, new_y, next_computer, distance + 1))

		elif status == 2:
			print(f"Shortest path: {distance + 1}")
			exit()
```
- The JavaScript version is as follows:
```javascript
const fs = require("fs");

const program = fs
	.readFileSync("input15", "utf-8")
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
		this.halted = false;
	}


	copy() {

		const computer = new Intcode([]);

		computer.memory = new Map(
			this.memory
		);

		computer.ip = this.ip;
		computer.relativeBase = this.relativeBase;
		computer.halted = this.halted;

		return computer;
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


	run(inputValue) {

		while (true) {

			const instruction = this.read(
				this.ip
			);

			const opcode = instruction % 100;

			const mode1 = Math.floor(
				instruction / 100
			) % 10;

			const mode2 = Math.floor(
				instruction / 1000
			) % 10;

			const mode3 = Math.floor(
				instruction / 10000
			) % 10;


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

				const address = this.writeAddress(
					mode1,
					this.ip + 1
				);

				this.write(
					address,
					inputValue
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

				if (
					this.parameter(
						mode1,
						this.ip + 1
					) !== 0
				) {

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

				if (
					this.parameter(
						mode1,
						this.ip + 1
					) === 0
				) {

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


const directions = new Map([
	[1, [0, -1]],
	[2, [0, 1]],
	[3, [-1, 0]],
	[4, [1, 0]]
]);


const computer = new Intcode(
	program
);


const queue = [];


queue.push({
	x: 0,
	y: 0,
	computer: computer,
	distance: 0
});


let queueIndex = 0;


const visited = new Set();

visited.add(
	"0,0"
);


while (queueIndex < queue.length) {

	const current = queue[
		queueIndex++
	];

	const x = current.x;
	const y = current.y;
	const currentComputer = current.computer;
	const distance = current.distance;


	for (const [command, [dx, dy]] of directions) {

		const newX = x + dx;
		const newY = y + dy;

		const key = `${newX},${newY}`;


		if (visited.has(key)) {
			continue;
		}


		const nextComputer = currentComputer.copy();


		const status = nextComputer.run(
			command
		);


		if (status === 0) {

			continue;
		}


		else if (status === 1) {

			visited.add(key);

			queue.push({
				x: newX,
				y: newY,
				computer: nextComputer,
				distance: distance + 1
			});
		}


		else if (status === 2) {

			console.log(
				`Shortest path: ${distance + 1}`
			);

			process.exit(0);
		}
	}
}
```
- This Solves The Part 01 of this challenge.
