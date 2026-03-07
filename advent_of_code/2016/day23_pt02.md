# URL
https://adventofcode.com/2016/day/23#part2

# Description
The safe doesn't open, but it does make several angry noises to express its frustration.

You're quite sure your logic is working correctly, so the only other thing is... you check the painting again. As it turns out, colored eggs are still eggs. Now you count 12.

As you run the program with this new input, the prototype computer begins to overheat. You wonder what's taking so long, and whether the lack of any instruction more powerful than "add one" has anything to do with it. Don't bunnies usually multiply?

Anyway, what value should actually be sent to the safe?

# Method of Solve
- The part 02 of this challenge can be solved using two methods :
- First is we can just replace 7 by 12 in the code but it is too slow as it computes actual factorial in assembly code:
  ```
    def get_value(x, registers):
        if x.lstrip("-").isdigit():
            return int(x)
        return registers[x]
    
    
    def run_program(filename, a_start=12):
        with open(filename) as f:
            program = [line.strip().split() for line in f]
    
        registers = {"a": a_start, "b": 0, "c": 0, "d": 0}
        i = 0
    
        while i < len(program):
            instr = program[i]
    
            if instr[0] == "cpy":
                x, y = instr[1], instr[2]
                if y in registers:
                    registers[y] = get_value(x, registers)
    
            elif instr[0] == "inc":
                registers[instr[1]] += 1
    
            elif instr[0] == "dec":
                registers[instr[1]] -= 1
    
            elif instr[0] == "jnz":
                x, y = instr[1], instr[2]
                if get_value(x, registers) != 0:
                    i += get_value(y, registers)
                    continue
    
            elif instr[0] == "tgl":
                x = get_value(instr[1], registers)
                target = i + x
    
                if 0 <= target < len(program):
                    t = program[target]
    
                    if len(t) == 2:
                        if t[0] == "inc":
                            t[0] = "dec"
                        else:
                            t[0] = "inc"
    
                    elif len(t) == 3:
                        if t[0] == "jnz":
                            t[0] = "cpy"
                        else:
                            t[0] = "jnz"
    
            i += 1
    
        return registers["a"]
    
    
    print("Part 2:", run_program("input_23", 12))
  ```
- Other way is that we calculate assembly values manually and multiply them
- NOTE : These values may differ from person to person's input
  ```
    import math
    
    a = 12
    result = math.factorial(a) + 85 * 76
    
    print(result)
  ```

# This Concludes Day 23 of The Advent of Code.
