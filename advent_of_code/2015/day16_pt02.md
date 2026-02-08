# URL
https://adventofcode.com/2015/day/16#part2

# Description
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

# Method of Solve
- The part 02 of the challenge can be solved using the code given below:
  ```
    target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
    }
    
    greater_than = {"cats", "trees"}
    less_than = {"pomeranians", "goldfish"}
    
    with open("input_16_01") as f:
        for line in f:
            name, rest = line.strip().split(": ", 1)
            sue_number = int(name.split()[1])
    
            props = {}
            for part in rest.split(", "):
                key, value = part.split(": ")
                props[key] = int(value)
    
            match = True
            for k, v in props.items():
                if k in greater_than:
                    if v <= target[k]:
                        match = False
                        break
                elif k in less_than:
                    if v >= target[k]:
                        match = False
                        break
                else:
                    if v != target[k]:
                        match = False
                        break
    
            if match:
                print("Correct Sue:", sue_number)
            break
  ```

# This Concludes the Day 16 of The Advent of Code
