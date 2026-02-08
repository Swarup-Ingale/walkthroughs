# URL
https://adventofcode.com/2015/day/18

# Description
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:
```
1B5...
234...
......
..123.
..8A4.
..765.
```
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
```
A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.
```
Here's a few steps from an example configuration of another 6x6 grid:
```
Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
```
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

# Method of Solve
- The parrt 01 of this challenge can be solved using the following code:
  ```
    def read_grid(filename):
        with open(filename) as f:
            return [list(line.strip()) for line in f]
    
    def count_neighbors(grid, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 100 and 0 <= ny < 100:
                    if grid[nx][ny] == "#":
                        count += 1
        return count
    
    grid = read_grid("input_18_01")
    
    for _ in range(100):
        new_grid = [row[:] for row in grid]
        for i in range(100):
            for j in range(100):
                neighbors = count_neighbors(grid, i, j)
                if grid[i][j] == "#":
                    if neighbors not in (2, 3):
                        new_grid[i][j] = "."
                else:
                    if neighbors == 3:
                        new_grid[i][j] = "#"
        grid = new_grid
    
    # Count lights that are ON
    answer = sum(row.count("#") for row in grid)
    print(answer)
  ```

# This Solves Part 01 of the challenge 
