# URL
https://adventofcode.com/2018/day/9#part2

# Description
Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble were 100 times larger?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re

class Node:

    def __init__(self, value):
        self.value = value
        self.prev = self
        self.next = self


with open("input_09") as f:
    players, last = map(
        int,
        re.findall(
            r"\d+",
            f.read()
        )
    )

last *= 100

scores = [0] * players

current = Node(0)

for marble in range(1, last + 1):

    player = marble % players

    if marble % 23 == 0:

        for _ in range(7):
            current = current.prev

        scores[player] += (
            marble +
            current.value
        )

        current.prev.next = (
            current.next
        )

        current.next.prev = (
            current.prev
        )

        current = current.next

    else:

        left = current.next
        right = left.next

        node = Node(marble)

        node.prev = left
        node.next = right

        left.next = node
        right.prev = node

        current = node

print(max(scores))
```
- The Javascript version is as follows:
```
const fs = require('fs');

const input =
    fs.readFileSync(
        'input_09',
        'utf8'
    );

const [players, lastRaw] =
    input.match(/\d+/g)
         .map(Number);

const last =
    lastRaw * 100;

class Node {

    constructor(value) {

        this.value = value;

        this.prev = this;
        this.next = this;
    }
}

const scores =
    Array(players).fill(0);

let current =
    new Node(0);

for (
    let marble = 1;
    marble <= last;
    marble++
) {

    const player =
        marble % players;

    if (marble % 23 === 0) {

        for (
            let i = 0;
            i < 7;
            i++
        ) {
            current =
                current.prev;
        }

        scores[player] +=
            marble +
            current.value;

        current.prev.next =
            current.next;

        current.next.prev =
            current.prev;

        current =
            current.next;

    } else {

        const left =
            current.next;

        const right =
            left.next;

        const node =
            new Node(marble);

        node.prev = left;
        node.next = right;

        left.next = node;
        right.prev = node;

        current = node;
    }
}

console.log(
    Math.max(...scores)
);
```

# This Concludes the Day 09 of The Advent of Code.
