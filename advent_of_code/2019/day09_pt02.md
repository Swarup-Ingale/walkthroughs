# URL
https://adventofcode.com/2019/day/9#part2

# Description
You now have a complete Intcode computer.

Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the BOOST program.

The program runs in sensor boost mode by providing the input instruction the value 2. Once run, it will boost the sensors automatically, but it might take a few seconds to complete the operation on slower hardware. In sensor boost mode, the program will output a single value: the coordinates of the distress signal.

Run the BOOST program in sensor boost mode. What are the coordinates of the distress signal?

# Method of Solve
- The Part 02 of this challenge can be solved as follows
- The Javascript version is as follows:
```
const fs = require("fs");

const program = fs
	.readFileSync("input09", "utf-8")
	.trim()
	.split(",")
	.map(Number);

const memory = new Map();

for (let i = 0; i < program.length; i++) {
	memory.set(i, program[i]);
}

function readMemory(address) {
	return memory.get(address) ?? 0;
}

function writeMemory(address, value) {
	memory.set(address, value);
}

let ip = 0;
let relativeBase = 0;

const inputs = [2];

function readParameter(mode, index) {
	if (mode === 0) {
		return readMemory(readMemory(index));
	}

	if (mode === 1) {
		return readMemory(index);
	}

	if (mode === 2) {
		return readMemory(relativeBase + readMemory(index));
	}

	throw new Error(`Invalid Parameter Mode: ${mode}`);
}


function writeAddress(mode, index) {
	if (mode === 0) {
		return readMemory(index);
	}

	if (mode === 2) {
		return relativeBase + readMemory(index);
	}

	throw new Error(`Invalid Write Parameter mode: ${mode}`);
}

while (true) {
	const instruction = readMemory(ip);

	const opcode = instruction % 100;

	const mode1 = Math.floor(instruction / 100) % 10;
	const mode2 = Math.floor(instruction / 1000) % 10;
	const mode3 = Math.floor(instruction / 10000) % 10;

	if (opcode === 99) {
		break;
	}

	else if (opcode === 1) {
		const a = readParameter(mode1, ip + 1);
		const b = readParameter(mode2, ip + 2);

		writeMemory(writeAddress(mode3, ip + 3), a + b);

		ip += 4;
	}

	else if (opcode === 2) {
		const a = readParameter(mode1, ip + 1);
		const b = readParameter(mode2, ip + 2);

		writeMemory(writeAddress(mode3, ip + 3), a * b);

		ip += 4;
	}

	else if (opcode === 3) {
		const value = inputs.shift();

		if (value === undefined) {
			throw new Error("Input required but none available.");
		}

		writeMemory(writeAddress(mode1, ip + 1), value);

		ip += 2;
	}

	else if (opcode === 4) {
		const output = readParameter(mode1, ip + 1);
		console.log(output);
		ip += 2;
	}

	else if (opcode === 5) {
		const condition = readParameter(mode1, ip + 1);

		if (condition !== 0) {
			ip = readParameter(mode2, ip + 2);
		}
		else {
			ip += 3;
		}
	}

	else if (opcode === 6) {
		const condition = readParameter(mode1, ip + 1);

		if (condition === 0) {
			ip = readParameter(mode2, ip + 2);
		}
		else {
			ip += 3;
		}
	}

	else if (opcode === 7) {
		const a = readParameter(mode1, ip + 1);
		const b = readParameter(mode2, ip + 2);

		writeMemory(writeAddress(mode3, ip + 3), a < b ? 1 : 0);

		ip += 4;
	}

	else if (opcode === 8) {
		const a = readParameter(mode1, ip + 1);
		const b = readParameter(mode2, ip + 2);

		writeMemory(writeAddress(mode3, ip + 3), a === b ? 1 : 0);

		ip += 4;
	}

	else if (opcode === 9) {
		relativeBase += readParameter(mode1, ip + 1);

		ip += 2;
	}

	else {
		throw new Error(`Unknown opcode: ${opcode} at position ${ip}`);
	}
}
```
- The Python version is as follows:
```
from collections import defaultdict

with open("input09", "r") as f:
    program = list(map(int, f.read().strip().split(",")))

memory = defaultdict(int)

for i, value in enumerate(program):
    memory[i] = value

ip = 0
relative_base = 0
inputs = [2]


def read(mode, index):
    if mode == 0:
        return memory[memory[index]]

    elif mode == 1:
        return memory[index]

    elif mode == 2:
        return memory[relative_base + memory[index]]

    else:
        raise ValueError(f"Invalid parameter mode: {mode}")


def write_addr(mode, index):
    if mode == 0:
        return memory[index]

    elif mode == 2:
        return relative_base + memory[index]

    else:
        raise ValueError(
            f"Invalid write parameter mode: {mode}"
        )


while True:
    instruction = memory[ip]

    opcode = instruction % 100

    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10
    mode3 = (instruction // 10000) % 10

    if opcode == 99:
        break

    elif opcode == 1:
        memory[write_addr(mode3, ip + 3)] = (
            read(mode1, ip + 1)
            + read(mode2, ip + 2)
        )

        ip += 4

    elif opcode == 2:
        memory[write_addr(mode3, ip + 3)] = (
            read(mode1, ip + 1)
            * read(mode2, ip + 2)
        )

        ip += 4

    elif opcode == 3:
        memory[write_addr(mode1, ip + 1)] = inputs.pop(0)

        ip += 2

    elif opcode == 4:
        print(read(mode1, ip + 1))

        ip += 2

    elif opcode == 5:
        if read(mode1, ip + 1) != 0:
            ip = read(mode2, ip + 2)
        else:
            ip += 3

    elif opcode == 6:
        if read(mode1, ip + 1) == 0:
            ip = read(mode2, ip + 2)
        else:
            ip += 3

    elif opcode == 7:
        memory[write_addr(mode3, ip + 3)] = int(
            read(mode1, ip + 1)
            < read(mode2, ip + 2)
        )

        ip += 4

    elif opcode == 8:
        memory[write_addr(mode3, ip + 3)] = int(
            read(mode1, ip + 1)
            == read(mode2, ip + 2)
        )

        ip += 4

    elif opcode == 9:
        relative_base += read(mode1, ip + 1)

        ip += 2

    else:
        raise ValueError(f"Unknown opcode: {opcode}")
```

# This Concludes Day 09 of The Advent of Code.
