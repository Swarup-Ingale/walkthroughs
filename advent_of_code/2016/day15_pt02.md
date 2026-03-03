# URL
https://adventofcode.com/2016/day/15#part2

# Description
After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it were time=0 again, but a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    def parse_input(filename):
        discs = []
    
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split()
    
                positions = int(parts[3])
                start_position = int(parts[-1].strip("."))
    
                discs.append((positions, start_position))
    
        return discs
    
    
    def find_first_time_part2(filename):
        discs = parse_input(filename)
    
        # Add the extra disc
        discs.append((11, 0))   # 11 positions, start at 0
    
        t = 0
    
        while True:
            success = True
    
            for i, (positions, start_position) in enumerate(discs, start=1):
                if (start_position + t + i) % positions != 0:
                    success = False
                    break
    
            if success:
                return t
    
            t += 1
    
    
    result = find_first_time_part2("input_15")
    print("First time to press button:", result)
  ```

# This Concludes the Day 15 of The Advent of Code.
