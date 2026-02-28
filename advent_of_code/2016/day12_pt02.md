# URL
https://adventofcode.com/2016/day/12#part2

# Description
As you head down the fire escape to the monorail, you notice it didn't start; register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1, what value is now left in register a?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    def run_assembunny_from_file(filename):
        
        with open("input_12", "r") as f:
            program = [line.strip().split() for line in f.readlines()]
    
        registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        ip = 0  # instruction pointer
    
        def get_value(x):
            if x.lstrip("-").isdigit():
                return int(x)
            return registers[x]
    
        while 0 <= ip < len(program):
            instruction = program[ip]
            op = instruction[0]
    
            if op == "cpy":
                x, y = instruction[1], instruction[2]
                registers[y] = get_value(x)
                ip += 1
    
            elif op == "inc":
                x = instruction[1]
                registers[x] += 1
                ip += 1
    
            elif op == "dec":
                x = instruction[1]
                registers[x] -= 1
                ip += 1
    
            elif op == "jnz":
                x, y = instruction[1], instruction[2]
                if get_value(x) != 0:
                    ip += get_value(y)
                else:
                    ip += 1
    
        return registers["a"]
    
    
    # Run the program
    result = run_assembunny_from_file("input.txt")
    print("Final value in register a:", result)
  ```

# This Concludes the Day 12 of The Advent of Code.
