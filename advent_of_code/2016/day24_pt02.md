# URL
https://adventofcode.com/2016/day/24#part2

# Description 
Of course, if you leave the cleaning robot somewhere weird, someone is bound to notice.

What is the fewest number of steps required to start at 0, visit every non-0 number marked on the map at least once, and then return to 0?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import deque
    from itertools import permutations
    
    
    def bfs(grid, start):
        rows = len(grid)
        cols = len(grid[0])
    
        q = deque([(start, 0)])
        visited = {start}
        dists = {}
    
        while q:
            (x, y), steps = q.popleft()
    
            if grid[y][x].isdigit():
                dists[int(grid[y][x])] = steps
    
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
    
                if 0 <= nx < cols and 0 <= ny < rows:
                    if grid[ny][nx] != "#" and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append(((nx, ny), steps + 1))
    
        return dists
    
    
    def solve(filename):
        grid = []
        locations = {}
    
        # Read grid
        with open(filename) as f:
            for y, line in enumerate(f):
                row = list(line.strip())
                grid.append(row)
    
                for x, c in enumerate(row):
                    if c.isdigit():
                        locations[int(c)] = (x, y)
    
        # Compute pairwise distances using BFS
        distances = {}
        for node, pos in locations.items():
            distances[node] = bfs(grid, pos)
    
        # All nodes except start
        nodes = list(locations.keys())
        nodes.remove(0)
    
        best = float("inf")
    
        # Try every visiting order
        for order in permutations(nodes):
            path = [0] + list(order)
    
            dist = 0
    
            for i in range(len(path) - 1):
                dist += distances[path[i]][path[i+1]]
    
            # Return to start
            dist += distances[path[-1]][0]
    
            best = min(best, dist)
    
        return best
    
    
    if __name__ == "__main__":
        result = solve("input_24")
        print("Part 2:", result)
  ```

# This Concludes Day 24 of The Advent of Code.
