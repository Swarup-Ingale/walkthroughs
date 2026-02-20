# URL
https://adventofcode.com/2016/day/1#part2

# Description
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def distance_to_first_revisited(filename):
        # Directions in order: North, East, South, West
        directions = ["N", "E", "S", "W"]
        dx = {"N": 0, "E": 1, "S": 0, "W": -1}
        dy = {"N": 1, "E": 0, "S": -1, "W": 0}
    
        x, y = 0, 0
        facing = 0  # start facing North
    
        visited = set()
        visited.add((0, 0))
    
        with open(filename, "r") as file:
            line = file.read().strip()
    
        instructions = line.split(",")
    
        for inst in instructions:
            inst = inst.strip()
            turn = inst[0]
            steps = int(inst[1:])
    
            if turn == "R":
                facing = (facing + 1) % 4
            else:  # "L"
                facing = (facing - 1) % 4
    
            direction = directions[facing]
    
            # Move ONE BLOCK AT A TIME
            for _ in range(steps):
                x += dx[direction]
                y += dy[direction]
    
                if (x, y) in visited:
                    return abs(x) + abs(y)
    
                visited.add((x, y))
    
        return None  # should never happen for valid inputs
    
    if __name__ == "__main__":
        result = distance_to_first_revisited("input_01")
        print("Distance to first location visited twice:", result)
  ```

# This Concludes Day 01 of The Advent of Code.
