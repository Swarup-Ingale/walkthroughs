# URL
https://adventofcode.com/2019/day/9

# Description
You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress signal coming from the asteroid belt. It must be the Ceres monitoring station!

In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest BOOST program - Basic Operation Of System Test.

While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous safety reasons, it refuses to do so until the computer it runs on passes some checks to demonstrate it is a complete Intcode computer.

Your existing Intcode computer is missing one key feature: it needs support for parameters in relative mode.

Parameters in mode 2, relative mode, behave very similarly to parameters in position mode: the parameter is interpreted as a position. Like position mode, parameters in relative mode can be read from or written to.

The important difference is that relative mode parameters don't count from address 0. Instead, they count from a value called the relative base. The relative base starts at 0.

The address a relative mode parameter refers to is itself plus the current relative base. When the relative base is 0, relative mode parameters and position mode parameters with the same value refer to the same address.

For example, given a relative base of 50, a relative mode parameter of -7 refers to memory address 50 + -7 = 43.

The relative base is modified with the relative base offset instruction:
```
    Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.
```
For example, if the relative base is 2000, then after the instruction 109,19, the relative base would be 2019. If the next instruction were 204,-34, then the value at address 1985 would be output.

Your Intcode computer will also need a few other capabilities:
```
    The computer's available memory should be much larger than the initial program. Memory beyond the initial program starts with the value 0 and can be read or written like any other memory. (It is invalid to try to access memory at a negative address, though.)
    The computer should have support for large numbers. Some instructions near the beginning of the BOOST program will verify this capability.
```
Here are some example programs that use these features:
```
    109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of itself as output.
    1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
    104,1125899906842624,99 should output the large number in the middle.
```
The BOOST program will ask for a single input; run it in test mode by providing it the value 1. It will perform a series of checks on each opcode, output any opcodes (and the associated parameter modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.

Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning opcodes when run in test mode; it should only output a single value, the BOOST keycode. What BOOST keycode does it produce?

# Method of Solve
- The Part 01 of this challenge can be solved as follows:
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
inputs = [1]


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

const inputs = [1];

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
- This Solves the Part 01 of this challenge.
