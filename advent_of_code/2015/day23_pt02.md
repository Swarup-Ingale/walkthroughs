# URL
https://adventofcode.com/2015/day/23#part2

# Description
The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def run_program(instructions):
        a, b = 1, 0
        ip = 0  # instruction pointer
    
        while 0 <= ip < len(instructions):
            inst = instructions[ip].replace(",", "").split()
    
            if inst[0] == "hlf":
                if inst[1] == "a":
                    a //= 2
                else:
                    b //= 2
                ip += 1
    
            elif inst[0] == "tpl":
                if inst[1] == "a":
                    a *= 3
                else:
                    b *= 3
                ip += 1
    
            elif inst[0] == "inc":
                if inst[1] == "a":
                    a += 1
                else:
                    b += 1
                ip += 1
    
            elif inst[0] == "jmp":
                ip += int(inst[1])
    
            elif inst[0] == "jie":
                r = a if inst[1] == "a" else b
                if r % 2 == 0:
                    ip += int(inst[2])
                else:
                    ip += 1
    
            elif inst[0] == "jio":
                r = a if inst[1] == "a" else b
                if r == 1:
                    ip += int(inst[2])
                else:
                    ip += 1
    
        return b
    
    
    # LOAD YOUR PUZZLE INPUT
    with open("input_23_01") as f:
        instructions = [line.strip() for line in f]
    
    print("Value in register b:", run_program(instructions))
  ```

# This Concludes the Day 23 of The Advent of Code.
