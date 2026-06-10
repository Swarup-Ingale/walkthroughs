# URL
https://adventofcode.com/2018/day/7

# Description
You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:
```
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
```
Visually, these requirements look like this:
```
  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----
```
Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:
```
    Only C is available, and so it is done first.
    Next, both A and F are available. A is first alphabetically, so it is done next.
    Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
    After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
    F is the only choice, so it is done next.
    Finally, E is completed.
```
So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version of the code is as follows:
```
import re
from collections import defaultdict

graph = defaultdict(set)
prereqs = defaultdict(set)
steps = set()

with open("input_07") as f:
    for line in f:
        a, b = re.match(
            r"Step ([A-Z]) must be finished before step ([A-Z]) can begin\.",
            line.strip()
        ).groups()

        graph[a].add(b)
        prereqs[b].add(a)

        steps.add(a)
        steps.add(b)

answer = []

while steps:

    available = sorted(
        step
        for step in steps
        if len(prereqs[step]) == 0
    )

    current = available[0]

    answer.append(current)
    steps.remove(current)

    for nxt in graph[current]:
        prereqs[nxt].remove(current)

print("".join(answer))
```
- The javascript version is as follows:
```
const fs = require('fs');

const lines = fs
    .readFileSync('input_07', 'utf8')
    .trim()
    .split('\n');

const graph = {};
const prereqs = {};
const steps = new Set();

for (const line of lines) {

    const [, a, b] =
        line.match(
            /Step ([A-Z]).*step ([A-Z])/
        );

    if (!graph[a]) graph[a] = [];
    if (!prereqs[a]) prereqs[a] = new Set();
    if (!prereqs[b]) prereqs[b] = new Set();

    graph[a].push(b);
    prereqs[b].add(a);

    steps.add(a);
    steps.add(b);
}

let answer = '';

while (steps.size) {

    const available =
        [...steps]
            .filter(
                s => prereqs[s].size === 0
            )
            .sort();

    const current = available[0];

    answer += current;
    steps.delete(current);

    if (graph[current]) {
        for (const nxt of graph[current]) {
            prereqs[nxt].delete(current);
        }
    }
}

console.log(answer);
```
- This solves the Part 01 of this challenge.
