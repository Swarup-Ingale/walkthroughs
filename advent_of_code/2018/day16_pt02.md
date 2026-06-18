# URL
https://adventofcode.com/2018/day/16#part2

# Description
Using the samples you collected, work out the number of each opcode and execute the test program (the second section of your puzzle input).

What value is contained in register 0 after executing the test program?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code :
- The Python version is as follows :
```

data = open("input_16").read()

ops = {
    "addr": lambda r,a,b,c: r.__setitem__(c, r[a] + r[b]),
    "addi": lambda r,a,b,c: r.__setitem__(c, r[a] + b),
    "mulr": lambda r,a,b,c: r.__setitem__(c, r[a] * r[b]),
    "muli": lambda r,a,b,c: r.__setitem__(c, r[a] * b),
    "banr": lambda r,a,b,c: r.__setitem__(c, r[a] & r[b]),
    "bani": lambda r,a,b,c: r.__setitem__(c, r[a] & b),
    "borr": lambda r,a,b,c: r.__setitem__(c, r[a] | r[b]),
    "bori": lambda r,a,b,c: r.__setitem__(c, r[a] | b),
    "setr": lambda r,a,b,c: r.__setitem__(c, r[a]),
    "seti": lambda r,a,b,c: r.__setitem__(c, a),
    "gtir": lambda r,a,b,c: r.__setitem__(c, int(a > r[b])),
    "gtri": lambda r,a,b,c: r.__setitem__(c, int(r[a] > b)),
    "gtrr": lambda r,a,b,c: r.__setitem__(c, int(r[a] > r[b])),
    "eqir": lambda r,a,b,c: r.__setitem__(c, int(a == r[b])),
    "eqri": lambda r,a,b,c: r.__setitem__(c, int(r[a] == b)),
    "eqrr": lambda r,a,b,c: r.__setitem__(c, int(r[a] == r[b]))
}

sample_part, program_part = data.split("\n\n\n\n")

samples = sample_part.strip().split("\n\n")

possible = {
    i: set(ops.keys())
    for i in range(16)
}

for sample in samples:

    before, instr, after = sample.splitlines()

    before = list(map(int, re.findall(r"\d+", before)))
    opcode, a, b, c = map(int, instr.split())
    after = list(map(int, re.findall(r"\d+", after)))

    for name, fn in ops.items():

        r = before[:]
        fn(r, a, b, c)

        if r != after:
            possible[opcode].discard(name)

mapping = {}

while len(mapping) < 16:

    progress = False

    for opcode in range(16):

        if len(possible[opcode]) == 1:

            op = next(iter(possible[opcode]))

            if opcode not in mapping:

                mapping[opcode] = op
                progress = True

                for other in range(16):
                    if other != opcode:
                        possible[other].discard(op)

    if not progress:
        break

reg = [0, 0, 0, 0]

for line in program_part.strip().splitlines():

    opcode, a, b, c = map(int, line.split())

    ops[mapping[opcode]](
        reg,
        a,
        b,
        c
    )

print(reg[0])
```
- The Javascript version is as follows :
```
const fs = require('fs');

const input = fs.readFileSync('input_16','utf8');

const ops = {
    addr:(r,a,b,c)=>r[c]=r[a]+r[b],
    addi:(r,a,b,c)=>r[c]=r[a]+b,
    mulr:(r,a,b,c)=>r[c]=r[a]*r[b],
    muli:(r,a,b,c)=>r[c]=r[a]*b,
    banr:(r,a,b,c)=>r[c]=r[a]&r[b],
    bani:(r,a,b,c)=>r[c]=r[a]&b,
    borr:(r,a,b,c)=>r[c]=r[a]|r[b],
    bori:(r,a,b,c)=>r[c]=r[a]|b,
    setr:(r,a,b,c)=>r[c]=r[a],
    seti:(r,a,b,c)=>r[c]=a,
    gtir:(r,a,b,c)=>r[c]=a>r[b]?1:0,
    gtri:(r,a,b,c)=>r[c]=r[a]>b?1:0,
    gtrr:(r,a,b,c)=>r[c]=r[a]>r[b]?1:0,
    eqir:(r,a,b,c)=>r[c]=a===r[b]?1:0,
    eqri:(r,a,b,c)=>r[c]=r[a]===b?1:0,
    eqrr:(r,a,b,c)=>r[c]=r[a]===r[b]?1:0
};

const [samplePart, programPart] =
    input.split('\n\n\n\n');

const samples =
    samplePart.trim().split('\n\n');

const possible = {};

for (let i = 0; i < 16; i++) {
    possible[i] =
        new Set(Object.keys(ops));
}

for (const sample of samples) {

    const lines =
        sample.split('\n');

    const before =
        lines[0].match(/\d+/g).map(Number);

    const [opcode,a,b,c] =
        lines[1].split(' ').map(Number);

    const after =
        lines[2].match(/\d+/g).map(Number);

    for (const [name, fn] of Object.entries(ops)) {

        const r = [...before];

        fn(r,a,b,c);

        if (
            JSON.stringify(r) !==
            JSON.stringify(after)
        ) {
            possible[opcode].delete(name);
        }
    }
}

const mapping = {};

while (
    Object.keys(mapping).length < 16
) {

    for (let i = 0; i < 16; i++) {

        if (
            possible[i].size === 1
        ) {

            const op =
                [...possible[i]][0];

            mapping[i] = op;

            for (let j = 0; j < 16; j++) {
                if (j !== i)
                    possible[j].delete(op);
            }
        }
    }
}

const reg = [0,0,0,0];

for (
    const line of
    programPart.trim().split('\n')
) {

    const [opcode,a,b,c] =
        line.split(' ').map(Number);

    ops[
        mapping[opcode]
    ](
        reg,
        a,
        b,
        c
    );
}

console.log(reg[0]);
```

# This Concludes Day 16 of The Advent of Code.
