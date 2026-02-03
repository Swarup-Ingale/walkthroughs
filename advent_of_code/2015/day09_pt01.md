# URL
https://adventofcode.com/2015/day/9

# Description
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:
```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```
The possible routes are therefore:
```
Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
```
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

# Method of Solve
- The Part 01 of the challenge can be solved by using the code written below:
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
    
    # Compute shortest route
    shortest = float("inf")
    
    for perm in itertools.permutations(cities):
        total = 0
        for i in range(len(perm) - 1):
            total += dist[perm[i]][perm[i + 1]]
        shortest = min(shortest, total)
    
    print(shortest)
  ```

# This Solves the Part 01 of the challenge.
