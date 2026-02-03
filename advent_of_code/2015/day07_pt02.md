# URL
https://adventofcode.com/2015/day/7#part2

# Description
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

# Method of Solve
The part 02 of the challenge can be solved using the code below:
  ```
    def evaluate(wire):
      if wire.isdigit():
          return int(wire)
  
      if wire in cache:
          return cache[wire]
  
      expr = instructions[wire].split()
  
      if len(expr) == 1:
          value = evaluate(expr[0])
  
      elif expr[0] == "NOT":
          value = ~evaluate(expr[1]) & 0xFFFF
  
      elif expr[1] == "AND":
          value = evaluate(expr[0]) & evaluate(expr[2])
  
      elif expr[1] == "OR":
          value = evaluate(expr[0]) | evaluate(expr[2])
  
      elif expr[1] == "LSHIFT":
          value = (evaluate(expr[0]) << int(expr[2])) & 0xFFFF
  
      elif expr[1] == "RSHIFT":
          value = evaluate(expr[0]) >> int(expr[2])
  
      cache[wire] = value
      return value
  
  
    # Parse input
    instructions = {}
    with open("input_07_01") as f:
        for line in f:
            left, right = line.strip().split(" -> ")
            instructions[right] = left
    
    # Part 01 solution logic remains same
    cache = {}
    a1 = evaluate("a")
    
    # override b and recompute
    instructions["b"] = str(a1)
    cache = {}
    print(evaluate("a"))
  ```

# This concludes Day 07 of Advent of code
