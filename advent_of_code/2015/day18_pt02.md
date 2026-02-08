# URL
https://adventofcode.com/2015/day/18#part2

# Description
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:
```
Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
```
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
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
    
    def force_corners(grid):
        grid[0][0] = "#"
        grid[0][99] = "#"
        grid[99][0] = "#"
        grid[99][99] = "#"
    
    grid = read_grid("input_18_01")
    
    # Force corners ON initially
    force_corners(grid)
    
    for _ in range(100):
        new_grid = [row[:] for row in grid]
        for i in range(100):
            for j in range(100):
                if (i, j) in [(0,0), (0,99), (99,0), (99,99)]:
                    continue  # corners stay ON
                neighbors = count_neighbors(grid, i, j)
                if grid[i][j] == "#":
                    if neighbors not in (2, 3):
                        new_grid[i][j] = "."
                else:
                    if neighbors == 3:
                        new_grid[i][j] = "#"
        force_corners(new_grid)
        grid = new_grid
    
    answer = sum(row.count("#") for row in grid)
    print(answer)
  ```

# This Concludes the Day 18 of The Advent of Code
