# URL
https://adventofcode.com/2017/day/22

# Description
Diagnostics indicate that the local grid computing cluster has been contaminated with the Sporifica Virus. The grid computing cluster is a seemingly-infinite two-dimensional grid of compute nodes. Each node is either clean or infected by the virus.


To prevent overloading the nodes (which would render them useless to the virus) or detection by system administrators, exactly one virus carrier moves through the network, infecting or cleaning nodes as it moves. The virus carrier is always located on a single node in the network (the current node) and keeps track of the direction it is facing.

To avoid detection, the virus carrier works in bursts; in each burst, it wakes up, does some work, and goes back to sleep. The following steps are all executed in order one time each burst:

If the current node is infected, it turns to its right. Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)
If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
The virus carrier moves forward one node in the direction it is facing.
Diagnostics have also provided a map of the node infection status (your puzzle input). Clean nodes are shown as .; infected nodes are shown as #. This map only shows the center of the grid; there are many more nodes beyond those shown, but none of them are currently infected.

The virus carrier begins in the middle of the map facing up.

For example, suppose you are given a map like this:
```
..#
#..
...
```
Then, the middle of the infinite grid looks like this, with the virus carrier's position marked with [ ]:
```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
The virus carrier is on a clean node, so it turns left, infects the node, and moves left:
```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]# . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
The virus carrier is on an infected node, so it turns right, cleans the node, and moves up:
```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
Four times in a row, the virus carrier finds a clean, infects it, turns left, and moves forward, ending in the same place and still facing up:
```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . #[#]. # . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
Now on the same node as before, it sees an infection, which causes it to turn right, clean the node, and move forward:
```
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . # .[.]# . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
After the above actions, a total of 7 bursts of activity had taken place. Of them, 5 bursts of activity caused an infection.

After a total of 70, the grid looks like this, with the virus carrier facing up:
```
. . . . . # # . .
. . . . # . . # .
. . . # . . . . #
. . # . #[.]. . #
. . # . # . . # .
. . . . . # # . .
. . . . . . . . .
. . . . . . . . .
```
By this time, 41 bursts of activity caused an infection (though most of those nodes have since been cleaned).

After a total of 10000 bursts of activity, 5587 bursts will have caused an infection.

Given your actual map, after 10000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)

# Method of Solve
- The Part 01 of this challeenge can be solved using the following code:
```
def turn_left(dx, dy):
    return -dy, dx

def turn_right(dx, dy):
    return dy, -dx


if __name__ == "__main__":
    grid = {}

    with open("input_22") as f:
        lines = [line.strip() for line in f]

    size = len(lines)
    offset = size // 2

    # store only infected nodes
    for i in range(size):
        for j in range(size):
            if lines[i][j] == '#':
                grid[(i - offset, j - offset)] = '#'

    x, y = 0, 0
    dx, dy = -1, 0  # facing UP

    infections = 0

    for _ in range(10000):
        if (x, y) in grid:  # infected
            dx, dy = turn_right(dx, dy)
            del grid[(x, y)]
        else:  # clean
            dx, dy = turn_left(dx, dy)
            grid[(x, y)] = '#'
            infections += 1

        x += dx
        y += dy

    print("Infections:", infections)
```
- This solves the Part 01 of this challenge.
