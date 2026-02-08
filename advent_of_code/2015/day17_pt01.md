# URL
https://adventofcode.com/2015/day/17

# Description
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:
```
15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
```
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

# Method of Solve
- The Part 01 of the challenge can be solved using the following code:
  ```
    import itertools

    containers = []
    with open("input_17_01") as f:
        for line in f:
            containers.append(int(line.strip()))
    
    target = 150
    count = 0
    
    for r in range(1, len(containers) + 1):
        for combo in itertools.combinations(containers, r):
            if sum(combo) == target:
                count += 1
    
    print(count)
  ```

# This Solves the part 01 of the challenge
