# URL
https://adventofcode.com/2016/day/13#part2

# Description
How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import deque
    
    def is_open(x, y, favorite_number):
        if x < 0 or y < 0:
            return False
    
        value = x*x + 3*x + 2*x*y + y + y*y
        value += favorite_number
    
        return bin(value).count("1") % 2 == 0
    
    
    def reachable_locations(filename, max_steps=50):
        # Read favorite number
        with open(filename, "r") as f:
            favorite_number = int(f.read().strip())
    
        start = (1, 1)
        queue = deque([(1, 1, 0)])  # (x, y, steps)
        visited = set()
        visited.add(start)
    
        while queue:
            x, y, steps = queue.popleft()
    
            if steps == max_steps:
                continue
    
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
    
                if (nx, ny) not in visited and is_open(nx, ny, favorite_number):
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    
        return len(visited)
    
    
    result = reachable_locations("input_13")
    print("Number of locations reachable in 50 steps:", result)
  ```

# This Concludes Day 13 of The Advent of Code.
