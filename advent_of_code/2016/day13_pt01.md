# URL


# Description
You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:
```
  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
```
Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:
```
  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
```
Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

# Method of Solve
- The part 01 of this challenge can be solved using the following code:
  ```
    from collections import deque
    
    def is_open(x, y, favorite_number):
        if x < 0 or y < 0:
            return False
    
        value = x*x + 3*x + 2*x*y + y + y*y
        value += favorite_number
    
        # Count 1 bits
        ones = bin(value).count("1")
    
        return ones % 2 == 0
    
    
    def shortest_path(filename, target_x=31, target_y=39):
        # Read favorite number using open()
        with open(filename, "r") as f:
            favorite_number = int(f.read().strip())
    
        start = (1, 1)
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
        visited = set()
        visited.add(start)
    
        while queue:
            x, y, steps = queue.popleft()
    
            if (x, y) == (target_x, target_y):
                return steps
    
            # Explore neighbors
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
    
                if (nx, ny) not in visited and is_open(nx, ny, favorite_number):
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    
        return -1  # Not reachable
    
    
    result = shortest_path("input_13")
    print("Fewest steps to reach (31,39):", result)
  ```
- This Solves the part 01 of the challenge.
