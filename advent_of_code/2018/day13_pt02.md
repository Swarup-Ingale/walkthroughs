# URL
https://adventofcode.com/2018/day/13#part2

# Description
There isn't much you can do to prevent crashes in this ridiculous system. However, by predicting the crashes, the Elves know where to be in advance and instantly remove the two crashing carts the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run out of carts. It could be useful to figure out where the last cart that hasn't crashed will end up.

For example:
```
/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/

/---\  
|   |  
| v-+-\
| | | |
\-+-/ |
  |   |
  ^---^

/---\  
|   |  
| /-+-\
| v | |
\-+-/ |
  ^   ^
  \---/

/---\  
|   |  
| /-+-\
| | | |
\-+-/ ^
  |   |
  \---/
```
After four very expensive crashes, a tick ends with only one cart remaining; its final location is 6,4.

What is the location of the last cart at the end of the first tick where it is the only cart left?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
grid = []
carts = []

with open("input_13") as f:
    for y, line in enumerate(f):
        row = list(line.rstrip("\n"))

        for x, c in enumerate(row):
            if c in "^v<>":
                carts.append([x, y, c, 0])  # x, y, dir, turn_state
                row[x] = "|" if c in "^v" else "-"

        grid.append(row)

dirs = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

left = {
    "^": "<",
    "<": "v",
    "v": ">",
    ">": "^"
}

right = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

slash = {
    "^": ">",
    ">": "^",
    "v": "<",
    "<": "v"
}

backslash = {
    "^": "<",
    "<": "^",
    "v": ">",
    ">": "v"
}

while len(carts) > 1:

    carts.sort(key=lambda c: (c[1], c[0]))

    removed = set()
    positions = {(c[0], c[1]): i for i, c in enumerate(carts)}

    for i, cart in enumerate(carts):

        if i in removed:
            continue

        positions.pop((cart[0], cart[1]), None)

        dx, dy = dirs[cart[2]]
        cart[0] += dx
        cart[1] += dy

        pos = (cart[0], cart[1])

        if pos in positions:
            removed.add(i)
            removed.add(positions[pos])
            positions.pop(pos, None)
            continue

        positions[pos] = i

        track = grid[cart[1]][cart[0]]

        if track == "/":
            cart[2] = slash[cart[2]]

        elif track == "\\":
            cart[2] = backslash[cart[2]]

        elif track == "+":
            if cart[3] == 0:
                cart[2] = left[cart[2]]
            elif cart[3] == 2:
                cart[2] = right[cart[2]]

            cart[3] = (cart[3] + 1) % 3

    carts = [c for i, c in enumerate(carts) if i not in removed]

print(f"{carts[0][0]},{carts[0][1]}")
```
- The Javascript version of code is :
```
const fs = require('fs');

const lines = fs.readFileSync('input_13', 'utf8').split('\n');
const grid = [], carts = [];

for (let y = 0; y < lines.length; y++) {
    const row = lines[y].replace(/\r$/, '').split('');

    for (let x = 0; x < row.length; x++) {
        const c = row[x];

        if ('^v<>'.includes(c)) {
            carts.push({ x, y, dir: c, turn: 0 });
            row[x] = '^v'.includes(c) ? '|' : '-';
        }
    }

    grid.push(row);
}

const dirs = {
    '^': [0, -1],
    'v': [0, 1],
    '<': [-1, 0],
    '>': [1, 0]
};

const left = {
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^'
};

const right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
};

const slash = {
    '^': '>',
    '>': '^',
    'v': '<',
    '<': 'v'
};

const backslash = {
    '^': '<',
    '<': '^',
    'v': '>',
    '>': 'v'
};

while (carts.length > 1) {

    carts.sort((a, b) => a.y - b.y || a.x - b.x);

    const removed = new Set();
    const pos = new Map();

    carts.forEach((c, i) => pos.set(`${c.x},${c.y}`, i));

    for (let i = 0; i < carts.length; i++) {

        if (removed.has(i)) continue;

        const cart = carts[i];

        pos.delete(`${cart.x},${cart.y}`);

        const [dx, dy] = dirs[cart.dir];
        cart.x += dx;
        cart.y += dy;

        const key = `${cart.x},${cart.y}`;

        if (pos.has(key)) {
            removed.add(i);
            removed.add(pos.get(key));
            pos.delete(key);
            continue;
        }

        pos.set(key, i);

        const track = grid[cart.y][cart.x];

        if (track === '/') {
            cart.dir = slash[cart.dir];
        } else if (track === '\\') {
            cart.dir = backslash[cart.dir];
        } else if (track === '+') {
            if (cart.turn === 0) cart.dir = left[cart.dir];
            else if (cart.turn === 2) cart.dir = right[cart.dir];

            cart.turn = (cart.turn + 1) % 3;
        }
    }

    for (let i = carts.length - 1; i >= 0; i--) {
        if (removed.has(i)) carts.splice(i, 1);
    }
}

console.log(`${carts[0].x},${carts[0].y}`);
```
# This Concludes Day 13 of The Advent of Code.
