# URL
https://adventofcode.com/2019/day/7#part2

# Description
It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a feedback loop:
```
      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
```
Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop: the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be sent to the thrusters using the new phase settings and feedback loop arrangement.

Here are some example programs:
```
    Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5

    Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

    3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
```
Try every combination of the new phase settings on the amplifier feedback loop. What is the highest signal that can be sent to the thrusters?

# Method of Solve
- The Part 02 of this challenge can be solved as follows:
- The Python version is as below:
```
import itertools
import os

class IntcodeComputer:
    def __init__(self, program):
        self.memory = program[:]
        self.pointer = 0
        self.inputs = []
        self.halted = False

    def run(self):
        while self.pointer < len(self.memory):
            opcode_mode = self.memory[self.pointer]
            opcode = opcode_mode % 100
            
            if opcode == 99:
                self.halted = True
                break

            def get_param(idx):
                mode = (opcode_mode // (10 ** (idx + 1))) % 10
                val = self.memory[self.pointer + idx]
                return val if mode == 1 else self.memory[val]

            if opcode == 1:
                self.memory[self.memory[self.pointer + 3]] = get_param(1) + get_param(2)
                self.pointer += 4
            elif opcode == 2:
                self.memory[self.memory[self.pointer + 3]] = get_param(1) * get_param(2)
                self.pointer += 4
            elif opcode == 3:
                if not self.inputs:
                    yield "NEED_INPUT"
                self.memory[self.memory[self.pointer + 1]] = self.inputs.pop(0)
                self.pointer += 2
            elif opcode == 4:
                out_val = get_param(1)
                self.pointer += 2
                yield out_val
            elif opcode == 5:
                self.pointer = get_param(2) if get_param(1) != 0 else self.pointer + 3
            elif opcode == 6:
                self.pointer = get_param(2) if get_param(1) == 0 else self.pointer + 3
            elif opcode == 7:
                self.memory[self.memory[self.pointer + 3]] = 1 if get_param(1) < get_param(2) else 0
                self.pointer += 4
            elif opcode == 8:
                self.memory[self.memory[self.pointer + 3]] = 1 if get_param(1) == get_param(2) else 0
                self.pointer += 4

def run_feedback_loop(program, phases):
    computers = [IntcodeComputer(program) for _ in range(5)]
    generators = [comp.run() for comp in computers]

    for i, phase in enumerate(phases):
        computers[i].inputs.append(phase)
        next(generators[i])

    signal = 0
    last_thruster_signal = 0
    amp_idx = 0

    while not computers[4].halted:
        comp = computers[amp_idx]
        gen = generators[amp_idx]
        comp.inputs.append(signal)
        
        try:
            res = next(gen)
            if res == "NEED_INPUT":
                res = next(gen)
            if isinstance(res, int):
                signal = res
                if amp_idx == 4:
                    last_thruster_signal = signal
        except StopIteration:
            pass

        amp_idx = (amp_idx + 1) % 5

    return last_thruster_signal

def solve():
    file_path = os.path.join(os.path.dirname(__file__), 'input07')
    
    with open(file_path, 'r') as file:
        puzzle_input = file.read()

    program = list(map(int, puzzle_input.strip().split(',')))
    max_signal = 0
    
    for phases in itertools.permutations(range(5, 10)):
        signal = run_feedback_loop(program, phases)
        max_signal = max(max_signal, signal)
    
    print(f"Part 2 Max Thruster Signal: {max_signal}")

if __name__ == "__main__":
    solve()
```
- The Javscript version is as below:
```
const fs = require('fs');
const path = require('path');

class IntcodeComputer {
    constructor(program) {
        this.memory = [...program];
        this.pointer = 0;
        this.inputs = [];
        this.halted = false;
    }

    run(newInputs = []) {
        this.inputs.push(...newInputs);

        while (this.pointer < this.memory.length) {
            const opcodeMode = this.memory[this.pointer];
            const opcode = opcodeMode % 100;

            if (opcode === 99) {
                this.halted = true;
                return null;
            }

            const getParam = (idx) => {
                const mode = Math.floor(opcodeMode / Math.pow(10, idx + 1)) % 10;
                const val = this.memory[this.pointer + idx];
                return mode === 1 ? val : this.memory[val];
            };

            switch (opcode) {
                case 1:
                    this.memory[this.memory[this.pointer + 3]] = getParam(1) + getParam(2);
                    this.pointer += 4;
                    break;
                case 2:
                    this.memory[this.memory[this.pointer + 3]] = getParam(1) * getParam(2);
                    this.pointer += 4;
                    break;
                case 3:
                    if (this.inputs.length === 0) {
                        return "WAITING_FOR_INPUT";
                    }
                    this.memory[this.memory[this.pointer + 1]] = this.inputs.shift();
                    this.pointer += 2;
                    break;
                case 4:
                    const outVal = getParam(1);
                    this.pointer += 2;
                    return outVal;
                case 5:
                    this.pointer = getParam(1) !== 0 ? getParam(2) : this.pointer + 3;
                    break;
                case 6:
                    this.pointer = getParam(1) === 0 ? getParam(2) : this.pointer + 3;
                    break;
                case 7:
                    this.memory[this.memory[this.pointer + 3]] = getParam(1) < getParam(2) ? 1 : 0;
                    this.pointer += 4;
                    break;
                case 8:
                    this.memory[this.memory[this.pointer + 3]] = getParam(1) === getParam(2) ? 1 : 0;
                    this.pointer += 4;
                    break;
            }
        }
    }
}

function permute(arr) {
    if (arr.length === 0) return [[]];
    let res = [];
    for (let i = 0; i < arr.length; i++) {
        let rest = permute(arr.slice(0, i).concat(arr.slice(i + 1)));
        for (let j = 0; j < rest.length; j++) {
            res.push([arr[i]].concat(rest[j]));
        }
    }
    return res;
}

function runFeedbackLoop(program, phases) {
    const comps = Array.from({ length: 5 }, () => new IntcodeComputer(program));
    
    for (let i = 0; i < 5; i++) {
        comps[i].run([phases[i]]);
    }

    let signal = 0;
    let lastThrusterSignal = 0;
    let ampIdx = 0;

    while (!comps[4].halted) {
        let res = comps[ampIdx].run([signal]);
        
        if (res !== null && res !== "WAITING_FOR_INPUT") {
            signal = res;
            if (ampIdx === 4) {
                lastThrusterSignal = signal;
            }
        }
        ampIdx = (ampIdx + 1) % 5;
    }

    return lastThrusterSignal;
}

function solve() {
    const filePath = path.join(__dirname, 'input07');
    const puzzleInput = fs.readFileSync(filePath, 'utf8');

    const program = puzzleInput.trim().split(',').map(Number);
    const allPhases = permute([5, 6, 7, 8, 9]);
    let maxSignal = 0;

    for (let phases of allPhases) {
        const signal = runFeedbackLoop(program, phases);
        if (signal > maxSignal) maxSignal = signal;
    }
    
    console.log(`Part 2 Max Thruster Signal: ${maxSignal}`);
}

solve();
```

# This Concludes Day 07 of The Advent of Code.
