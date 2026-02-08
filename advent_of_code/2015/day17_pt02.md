# URL
https://adventofcode.com/2015/day/17#part2

# Description
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    import itertools

    containers = []
    with open("input_17_01") as f:
        for line in f:
            containers.append(int(line.strip()))
    
    target = 150
    valid_lengths = []
    
    # Find all valid combinations and record their lengths
    for r in range(1, len(containers) + 1):
        for combo in itertools.combinations(containers, r):
            if sum(combo) == target:
                valid_lengths.append(len(combo))
    
    # Step 1: minimum number of containers
    min_len = min(valid_lengths)
    
    # Step 2: count combinations that use that minimum
    answer = valid_lengths.count(min_len)
    
    print(answer)
  ```

# This Concludes the Day 17 of The Advent of Code
