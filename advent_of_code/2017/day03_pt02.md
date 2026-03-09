# URL
https://adventofcode.com/2017/day/3#part2

# Description
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:
```
Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
```
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:
```
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
```
What is the first value written that is larger than your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import defaultdict
    
    # Read puzzle input
    with open("input_03", "r") as f:
        target = int(f.read().strip())
    
    grid = defaultdict(int)
    x, y = 0, 0
    grid[(x, y)] = 1
    
    # Spiral directions: right, up, left, down
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    step_size = 1
    
    while True:
        for d in range(4):
            dx, dy = directions[d]
    
            for _ in range(step_size):
                x += dx
                y += dy
    
                value = 0
    
                # Sum all neighbors
                for nx in [-1,0,1]:
                    for ny in [-1,0,1]:
                        if nx == 0 and ny == 0:
                            continue
                        value += grid[(x+nx, y+ny)]
    
                grid[(x,y)] = value
    
                if value > target:
                    print(value)
                    exit()
    
            # Increase steps after every two directions
            if d % 2 == 1:
                step_size += 1
  ```

# This Concludes Day 03 of The Advent of Code.
