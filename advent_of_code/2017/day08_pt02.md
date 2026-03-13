# URL
https://adventofcode.com/2017/day/8#part2

# Description
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import defaultdict
    
    registers = defaultdict(int)
    highest = 0
    
    with open("input_08", "r") as f:
        for line in f:
            reg, op, val, _, cond_reg, cond_op, cond_val = line.split()
    
            val = int(val)
            cond_val = int(cond_val)
    
            if eval(f"{registers[cond_reg]} {cond_op} {cond_val}"):
    
                if op == "inc":
                    registers[reg] += val
                else:
                    registers[reg] -= val
    
                highest = max(highest, registers[reg])
    
    print(highest)
  ```

# This Concludes Day 08 of The Advent of Code.
