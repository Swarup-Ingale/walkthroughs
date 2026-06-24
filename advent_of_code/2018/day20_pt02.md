# URL
https://adventofcode.com/2018/day/20#part2

# Description
Okay, so the facility is big.

How many rooms have a shortest path from your current location that pass through at least 1000 doors?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
regex = open("input_20").read().strip()[1:-1]

dirs = {
    "N": (0, -1),
    "S": (0, 1),
    "E": (1, 0),
    "W": (-1, 0)
}

graph = {}

def add(a, b):

    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set()).add(a)

pos = {(0, 0)}
stack = []

for c in regex:

    if c in "NESW":

        nxt = set()

        for x, y in pos:

            dx, dy = dirs[c]

            nx = x + dx
            ny = y + dy

            add((x, y), (nx, ny))

            nxt.add((nx, ny))

        pos = nxt

    elif c == "(":

        stack.append(
            (set(pos), set())
        )

    elif c == "|":

        start, end = stack[-1]

        end.update(pos)

        pos = set(start)

    elif c == ")":

        start, end = stack.pop()

        end.update(pos)

        pos = end

from collections import deque

q = deque([((0, 0), 0)])

seen = {(0, 0)}

part1 = 0
part2 = 0

while q:

    node, d = q.popleft()

    part1 = max(part1, d)

    if d >= 1000:
        part2 += 1

    for nxt in graph[node]:

        if nxt in seen:
            continue

        seen.add(nxt)

        q.append((nxt, d + 1))

print(part1)
print(part2)
```
- The Javascript version is as follows:
```const fs = require('fs');

const regex = fs.readFileSync('input_20', 'utf8')
    .trim()
    .slice(1, -1);

const dirs = {
    N: [0, -1],
    S: [0, 1],
    E: [1, 0],
    W: [-1, 0]
};

const graph = new Map();

function add(a, b) {

    if (!graph.has(a))
        graph.set(a, new Set());

    if (!graph.has(b))
        graph.set(b, new Set());

    graph.get(a).add(b);
    graph.get(b).add(a);
}

let pos = new Set(["0,0"]);
const stack = [];

for (const c of regex) {

    if ("NESW".includes(c)) {

        const next = new Set();

        for (const p of pos) {

            const [x, y] =
                p.split(',').map(Number);

            const [dx, dy] =
                dirs[c];

            const nx = x + dx;
            const ny = y + dy;

            const np = `${nx},${ny}`;

            add(p, np);

            next.add(np);
        }

        pos = next;
    }

    else if (c === '(') {

        stack.push([
            new Set(pos),
            new Set()
        ]);
    }

    else if (c === '|') {

        const top =
            stack[stack.length - 1];

        for (const p of pos)
            top[1].add(p);

        pos = new Set(top[0]);
    }

    else if (c === ')') {

        const [_, end] =
            stack.pop();

        for (const p of pos)
            end.add(p);

        pos = end;
    }
}

const q = [["0,0", 0]];
const seen = new Set(["0,0"]);

let part1 = 0;
let part2 = 0;

while (q.length) {

    const [node, d] = q.shift();

    part1 = Math.max(part1, d);

    if (d >= 1000)
        part2++;

    for (const nxt of graph.get(node)) {

        if (seen.has(nxt))
            continue;

        seen.add(nxt);

        q.push([nxt, d + 1]);
    }
}

console.log("Part 1:", part1);
console.log("Part 2:", part2);
```

# This Concludes Day 20 of The Advent of Code.
