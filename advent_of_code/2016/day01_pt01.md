# URL
https://adventofcode.com/2016/day/1

# Description
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:
```
Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
```
How many blocks away is Easter Bunny HQ?

# Method of Solve
- This challenge can be solved using the following code:
  ```
    def distance_to_hq_from_file(filename):
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        facing = 0  # start facing North
        x, y = 0, 0
    
        with open(filename, "r") as f:
            instructions = f.read().strip()
    
        for step in instructions.split(", "):
            turn = step[0]
            blocks = int(step[1:])
    
            if turn == "R":
                facing = (facing + 1) % 4
            else:  # "L"
                facing = (facing - 1) % 4
    
            dx, dy = directions[facing]
            x += dx * blocks
            y += dy * blocks
    
        return abs(x) + abs(y)
    
    print("Blocks away:", distance_to_hq_from_file("input_01"))
  ```
- This Solves the part 01 of the challenge.

