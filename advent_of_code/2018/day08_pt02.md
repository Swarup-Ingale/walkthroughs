# URL
https://adventofcode.com/2018/day/8#part2

# Description
The second check is slightly more complicated: you need to find the value of the root node (A in the example above).

The value of a node depends on whether it has child nodes.

If a node has no child nodes, its value is the sum of its metadata entries. So, the value of node B is 10+11+12=33, and the value of node D is 99.

However, if a node does have child nodes, the metadata entries become indexes which refer to those child nodes. A metadata entry of 1 refers to the first child node, 2 to the second, 3 to the third, and so on. The value of this node is the sum of the values of the child nodes referenced by the metadata entries. If a referenced child node does not exist, that reference is skipped. A child node can be referenced multiple time and counts each time it is referenced. A metadata entry of 0 does not refer to any child node.

For example, again using the above nodes:
```
    Node C has one metadata entry, 2. Because node C has only one child node, 2 references a child node which does not exist, and so the value of node C is 0.
    Node A has three metadata entries: 1, 1, and 2. The 1 references node A's first child node, B, and the 2 references node A's second child node, C. Because node B has a value of 33 and node C has a value of 0, the value of node A is 33+33+0=66.
```
So, in this example, the value of the root node is 66.

What is the value of the root node?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input_08") as f:
    data = list(map(int, f.read().split()))

idx = 0

def value():

    global idx

    children = data[idx]
    metadata = data[idx + 1]

    idx += 2

    child_values = []

    for _ in range(children):
        child_values.append(
            value()
        )

    entries = data[
        idx : idx + metadata
    ]

    idx += metadata

    if children == 0:
        return sum(entries)

    total = 0

    for ref in entries:

        if (
            1 <= ref <= children
        ):
            total += child_values[
                ref - 1
            ]

    return total

print(value())
```
- The Javascript version is as follows:
```
const fs = require('fs');

const data = fs
    .readFileSync('input_08', 'utf8')
    .trim()
    .split(/\s+/)
    .map(Number);

let idx = 0;

function value() {

    const children =
        data[idx++];

    const metadata =
        data[idx++];

    const childValues = [];

    for (
        let i = 0;
        i < children;
        i++
    ) {
        childValues.push(
            value()
        );
    }

    const entries = [];

    for (
        let i = 0;
        i < metadata;
        i++
    ) {
        entries.push(
            data[idx++]
        );
    }

    if (children === 0) {

        return entries.reduce(
            (a, b) => a + b,
            0
        );
    }

    let total = 0;

    for (const ref of entries) {

        if (
            ref >= 1 &&
            ref <= children
        ) {
            total +=
                childValues[
                    ref - 1
                ];
        }
    }

    return total;
}

console.log(value());
```

# This Concludes Day 08 of The Advent of Code.

