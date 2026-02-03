# URL
https://adventofcode.com/2015/day/9#part2

# Description
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example : 
```
given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
```
What is the distance of the longest route?

# Method of Solve
- This is Part 02 of the Challenge and can be solved using the code given below:
  ```
    import itertools

    dist = {}
    cities = set()
    
    # Parse input
    with open("input_09_01") as f:
        for line in f:
            parts = line.strip().split()
            a, b = parts[0], parts[2]
            d = int(parts[4])
    
            cities.add(a)
            cities.add(b)
    
            dist.setdefault(a, {})[b] = d
            dist.setdefault(b, {})[a] = d
    
    # Compute longest route
    longest = 0
    
    for perm in itertools.permutations(cities):
        total = 0
        for i in range(len(perm) - 1):
            total += dist[perm[i]][perm[i + 1]]
        longest = max(longest, total)
    
    print(longest)
  ```

# This Concludes the Advent of Code Challenge for Day 09.
