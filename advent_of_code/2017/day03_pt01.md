# URL
https://adventofcode.com/2017/day/3

# Description 
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:
```
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
```
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:
```
Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
```
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    import math
    
    def spiral_distance(n):
        if n == 1:
            return 0
    
        # Determine ring layer
        k = math.ceil((math.sqrt(n) - 1) / 2)
    
        # Maximum value in this ring
        max_val = (2 * k + 1) ** 2
    
        side_len = 2 * k
    
        # Midpoints of each side of the ring
        midpoints = [
            max_val - k,
            max_val - k - side_len,
            max_val - k - 2 * side_len,
            max_val - k - 3 * side_len
        ]
    
        # Distance from closest midpoint
        offset = min(abs(n - m) for m in midpoints)
    
        return k + offset
    
    
    # Read puzzle input
    with open("input_03", "r") as f:
        number = int(f.read().strip())
    
    result = spiral_distance(number)
    
    print(result)
  ```
- This Solves the Part 01 of this challenge.
