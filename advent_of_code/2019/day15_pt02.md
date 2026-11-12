# URL
https://adventofcode.com/2019/day/15#part2

# Description
--- Part Two ---

You quickly repair the oxygen system; oxygen gradually fills the area.

Oxygen starts in the location containing the repaired oxygen system. It takes one minute for oxygen to spread to all open locations that are adjacent to a location that already contains oxygen. Diagonal locations are not adjacent.

In the example above, suppose you've used the droid to explore the area fully and have the following map (where locations that currently contain oxygen are marked O):

 ##   
#..## 
#.#..#
#.O.# 
 ###  


Initially, the only location which contains oxygen is the location of the repaired oxygen system. However, after one minute, the oxygen spreads to all open (.) locations that are adjacent to a location containing oxygen:

 ##   
#..## 
#.#..#
#OOO# 
 ###  


After a total of two minutes, the map looks like this:

 ##   
#..## 
#O#O.#
#OOO# 
 ###  


After a total of three minutes:

 ##   
#O.## 
#O#OO#
#OOO# 
 ###  


And finally, the whole region is full of oxygen after a total of four minutes:

 ##   
#OO## 
#O#OO#
#OOO# 
 ###  


So, in this example, all locations contain oxygen after 4 minutes.

Use the repair droid to get a complete map of the area. How many minutes will it take to fill with oxygen?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```python
from collections import defaultdict, deque


with open("input15", "r") as f:
	program = list(
		map(
			int,
			f.read().strip().split(",")
		)
	)


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

				address = self.write_address(
					mode1,
					self.ip + 1
				)

				self.write(
					address,
					input_value
				)

				self.ip += 2


			elif opcode == 4:

				output = self.parameter(
					mode1,
					self.ip + 1
				)

				self.ip += 2

				return output


			elif opcode == 5:

				if self.parameter(
					mode1,
					self.ip + 1
				) != 0:

					self.ip = self.parameter(
						mode2,
						self.ip + 2
					)

				else:

					self.ip += 3


			elif opcode == 6:

				if self.parameter(
					mode1,
					self.ip + 1
				) == 0:

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
					f"Unknown opcode {opcode} at position {self.ip}"
				)


directions = {
	1: (0, -1),
	2: (0, 1),
	3: (-1, 0),
	4: (1, 0)
}


computer = Intcode(program)


queue = deque()

queue.append(
	(
		0,
		0,
		computer
	)
)


visited = set()

visited.add(
	(0, 0)
)


area = {
	(0, 0): 1
}


oxygen = None


while queue:

	x, y, computer = queue.popleft()


	for command, (dx, dy) in directions.items():

		new_x = x + dx
		new_y = y + dy


		if (new_x, new_y) in visited:
			continue


		next_computer = computer.copy()


		status = next_computer.run(
			command
		)


		if status == 0:

			area[
				(new_x, new_y)
			] = 0

			continue


		elif status == 1:

			visited.add(
				(new_x, new_y)
			)

			area[
				(new_x, new_y)
			] = 1

			queue.append(
				(
					new_x,
					new_y,
					next_computer
				)
			)


		elif status == 2:

			visited.add(
				(new_x, new_y)
			)

			area[
				(new_x, new_y)
			] = 2

			oxygen = (
				new_x,
				new_y
			)

			queue.append(
				(
					new_x,
					new_y,
					next_computer
				)
			)


if oxygen is None:

	raise RuntimeError(
		"Oxygen system was not found."
	)


queue = deque()

queue.append(
	(
		oxygen[0],
		oxygen[1],
		0
	)
)


visited = set()

visited.add(
	oxygen
)


max_distance = 0


while queue:

	x, y, distance = queue.popleft()


	max_distance = max(
		max_distance,
		distance
	)


	for dx, dy in directions.values():

		new_x = x + dx
		new_y = y + dy


		if (new_x, new_y) in visited:
			continue


		if area.get(
			(new_x, new_y),
			0
		) == 0:

			continue


		visited.add(
			(new_x, new_y)
		)

		queue.append(
			(
				new_x,
				new_y,
				distance + 1
			)
		)


print(
	f"Oxygen fill time: {max_distance}"
)
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


function key(x, y) {
	return `${x},${y}`;
}


const computer = new Intcode(
	program
);


const queue = [];

queue.push({
	x: 0,
	y: 0,
	computer: computer
});


let queueIndex = 0;


const visited = new Set();

visited.add(
	key(0, 0)
);


const area = new Map();

area.set(
	key(0, 0),
	1
);


let oxygen = null;


while (queueIndex < queue.length) {

	const current = queue[
		queueIndex++
	];

	const x = current.x;
	const y = current.y;
	const currentComputer = current.computer;


	for (const [command, [dx, dy]] of directions) {

		const newX = x + dx;
		const newY = y + dy;

		const newKey = key(
			newX,
			newY
		);


		if (visited.has(newKey)) {
			continue;
		}


		const nextComputer = currentComputer.copy();


		const status = nextComputer.run(
			command
		);


		if (status === 0) {

			area.set(
				newKey,
				0
			);

			continue;
		}


		else if (status === 1) {

			visited.add(newKey);

			area.set(
				newKey,
				1
			);

			queue.push({
				x: newX,
				y: newY,
				computer: nextComputer
			});
		}


		else if (status === 2) {

			visited.add(newKey);

			area.set(
				newKey,
				2
			);

			oxygen = {
				x: newX,
				y: newY
			};

			queue.push({
				x: newX,
				y: newY,
				computer: nextComputer
			});
		}
	}
}


if (oxygen === null) {

	throw new Error(
		"Oxygen system was not found."
	);
}


const oxygenQueue = [];

oxygenQueue.push({
	x: oxygen.x,
	y: oxygen.y,
	distance: 0
});


let oxygenQueueIndex = 0;


const oxygenVisited = new Set();

oxygenVisited.add(
	key(
		oxygen.x,
		oxygen.y
	)
);


let maxDistance = 0;


while (
	oxygenQueueIndex < oxygenQueue.length
) {

	const current = oxygenQueue[
		oxygenQueueIndex++
	];

	const x = current.x;
	const y = current.y;
	const distance = current.distance;


	maxDistance = Math.max(
		maxDistance,
		distance
	);


	for (const [dx, dy] of directions.values()) {

		const newX = x + dx;
		const newY = y + dy;

		const newKey = key(
			newX,
			newY
		);


		if (oxygenVisited.has(newKey)) {
			continue;
		}


		if (
			(area.get(newKey) ?? 0) === 0
		) {
			continue;
		}


		oxygenVisited.add(newKey);

		oxygenQueue.push({
			x: newX,
			y: newY,
			distance: distance + 1
		});
	}
}


console.log(
	`Oxygen fill time: ${maxDistance}`
);
```
- This Concludes Day 15 of The Advent of Code.
