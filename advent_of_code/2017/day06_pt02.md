# URL
https://adventofcode.com/2017/day/6#part2

# Description
Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    with open("input_06", "r") as f:
        banks = list(map(int, f.read().strip().split()))
    
    seen = {}
    cycles = 0
    
    while tuple(banks) not in seen:
        seen[tuple(banks)] = cycles
    
        # Find bank with maximum blocks
        idx = banks.index(max(banks))
        blocks = banks[idx]
        banks[idx] = 0
    
        i = idx
        while blocks > 0:
            i = (i + 1) % len(banks)
            banks[i] += 1
            blocks -= 1
    
        cycles += 1
    
    # Calculate loop size
    loop_size = cycles - seen[tuple(banks)]
    
    print(loop_size)
  ```

# This Concludes Day 06 of The Advent of Code.
