# URL
https://adventofcode.com/2017/day/11

# Description 
Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:
```
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
```
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

- ne,ne,ne is 3 steps away.
- ne,ne,sw,sw is 0 steps away (back where you started).
- ne,ne,s,s is 2 steps away (se,se).
- se,sw,se,sw,sw is 3 steps away (s,s,sw).

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
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
print("Part 1:", dist)
```
- This Solves the Part 01 of this challenge.
