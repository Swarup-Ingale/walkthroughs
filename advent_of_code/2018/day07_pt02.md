# URL
https://adventofcode.com/2018/day/7#part2

# Description
As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:
```
Second   Worker 1   Worker 2   Done
   0        C          .        
   1        C          .        
   2        C          .        
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE
```
Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these steps.

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re
from collections import defaultdict

WORKERS = 5
BASE = 60

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

workers = []
time = 0

while steps or workers:

    available = sorted(
        s for s in steps
        if len(prereqs[s]) == 0
        and s not in [job for _, job in workers]
    )

    while (
        available
        and len(workers) < WORKERS
    ):
        step = available.pop(0)

        duration = (
            BASE
            + ord(step)
            - ord('A')
            + 1
        )

        workers.append(
            [time + duration, step]
        )

    workers.sort()

    finish_time, done = workers.pop(0)

    time = finish_time
    steps.remove(done)

    for nxt in graph[done]:
        prereqs[nxt].remove(done)

print(time)
```
- The Javascript version is as follows:
```
const fs = require('fs');

const lines = fs
    .readFileSync('input_07', 'utf8')
    .trim()
    .split('\n');

const WORKERS = 5;
const BASE = 60;

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

let workers = [];
let time = 0;

while (
    steps.size > 0 ||
    workers.length > 0
) {

    const busy =
        workers.map(w => w.step);

    const available =
        [...steps]
            .filter(
                s =>
                    prereqs[s].size === 0 &&
                    !busy.includes(s)
            )
            .sort();

    while (
        available.length &&
        workers.length < WORKERS
    ) {

        const step =
            available.shift();

        const duration =
            BASE +
            step.charCodeAt(0) -
            64;

        workers.push({
            finish:
                time + duration,
            step
        });
    }

    workers.sort(
        (a, b) =>
            a.finish - b.finish
    );

    const finished =
        workers.shift();

    time = finished.finish;

    steps.delete(
        finished.step
    );

    if (graph[finished.step]) {

        for (
            const nxt of graph[
                finished.step
            ]
        ) {
            prereqs[nxt].delete(
                finished.step
            );
        }
    }
}

console.log(time);
```

# This concludes The Day 07 of The Advent of Code.
