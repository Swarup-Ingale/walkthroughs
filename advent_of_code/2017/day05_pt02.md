# URL
http://adventofcode.com/2017/day/5#part2  

# Description
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    with open("input_05", "r") as f:
        jumps = [int(x.strip()) for x in f]
    
    index = 0
    steps = 0
    
    while 0 <= index < len(jumps):
        jump = jumps[index]
    
        if jump >= 3:
            jumps[index] -= 1
        else:
            jumps[index] += 1
    
        index += jump
        steps += 1
    
    print(steps)
  ```

# This Concludes Day 05 of The Advent of Code.
