# URL
https://adventofcode.com/2017/day/19#part2

# Description
The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...
```
     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 
```
...the packet would go:

- 6 steps down (including the first line at the top of the diagram).
- 3 steps right.
- 4 steps up.
- 3 steps right.
- 4 steps down.
- 3 steps right.
- 2 steps up.
- 13 steps left (including the F it stops on).

This would result in a total of 38 steps.

How many steps does the packet need to go?

# Method Of Solve
- The Part 02 of this challenge can be solved using the following code:
```
def part2(grid):
    rows = len(grid)
    cols = len(grid[0])

    x = 0
    y = grid[0].index('|')

    dx, dy = 1, 0
    steps = 0

    while True:
        x += dx
        y += dy
        steps += 1

        if x < 0 or y < 0 or x >= rows or y >= cols:
            break

        char = grid[x][y]

        if char == ' ':
            break

        if char == '+':
            for ndx, ndy in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (ndx, ndy) != (-dx, -dy):
                    nx, ny = x + ndx, y + ndy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] != ' ':
                            dx, dy = ndx, ndy
                            break

    return steps


if __name__ == "__main__":
    with open("input_19") as f:
        grid = [list(line.rstrip('\n')) for line in f]

    print("Steps:", part2(grid))
```

# This Concludes Day 19 of The Advent of Code.
