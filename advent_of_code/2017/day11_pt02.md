# URL
https://adventofcode.com/2017/day/11#part2

# Description
How many steps away is the furthest he ever got from his starting position?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
with open("input_11") as f:
    steps = f.read().strip().split(",")

# cube coordinates
x = y = z = 0

# track max distance
max_dist = 0

moves = {
    "n":  (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s":  (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0)
}

for step in steps:
    dx, dy, dz = moves[step]

    x += dx
    y += dy
    z += dz

    dist = max(abs(x), abs(y), abs(z))
    max_dist = max(max_dist, dist)

print("Part 2:", max_dist)
```

# This Concludes Day 11 of The Advent of Code.
