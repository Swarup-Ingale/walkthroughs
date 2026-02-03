# URL
https://adventofcode.com/2015/day/7

# Description
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:
```
123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
```
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:
```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```
After it is run, these are the signals on the wires:
```
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# Method of Solve
The below given code can be used to solve the Part 01 of the Challenge:
  ```
    def evaluate(wire):
      if wire.isdigit():
          return int(wire)
  
      if wire in cache:
          return cache[wire]
  
      expression = instructions[wire].split()
  
      if len(expression) == 1:
          value = evaluate(expression[0])
  
      elif expression[0] == "NOT":
          value = ~evaluate(expression[1]) & 0xFFFF
  
      elif expression[1] == "AND":
          value = evaluate(expression[0]) & evaluate(expression[2])
  
      elif expression[1] == "OR":
          value = evaluate(expression[0]) | evaluate(expression[2])
  
      elif expression[1] == "LSHIFT":
          value = (evaluate(expression[0]) << int(expression[2])) & 0xFFFF
  
      elif expression[1] == "RSHIFT":
          value = evaluate(expression[0]) >> int(expression[2])
  
      cache[wire] = value
      return value
  
  
    instructions = {}
    cache = {}
    
    with open("input_07_01") as f:
        for line in f:
            left, right = line.strip().split(" -> ")
            instructions[right] = left
    
    print(evaluate("a"))
  ```
- This solves the first part of the challenge
