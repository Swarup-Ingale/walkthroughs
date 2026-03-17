# URL
https://adventofcode.com/2017/day/12#part2

# Description
There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
from collections import defaultdict, deque

graph = defaultdict(list)

with open("input_12") as f:
    for line in f:
        left, right = line.strip().split(" <-> ")
        node = int(left)
        neighbors = list(map(int, right.split(", ")))
        graph[node] = neighbors

visited = set()
groups = 0

for node in graph:
    if node not in visited:
        groups += 1
        queue = deque([node])

        while queue:
            n = queue.popleft()

            if n not in visited:
                visited.add(n)
                queue.extend(graph[n])

print(groups)
```

# This Concludes Day 12 of The Advent of Code.
