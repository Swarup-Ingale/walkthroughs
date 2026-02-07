# URL
https://adventofcode.com/2015/day/13#part2

# Description
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

# Method of Solve
- The part 02 of the challenge can be solved using the following code:
  ```
    import itertools
    import re
    
    happiness = {}
    people = set()
    
    # Parse input
    with open("input_13_01") as f:
        for line in f:
            m = re.match(
                r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).",
                line.strip()
            )
            a, sign, value, b = m.groups()
            value = int(value)
            if sign == "lose":
                value = -value
    
            people.add(a)
            people.add(b)
            happiness.setdefault(a, {})[b] = value
    
    # Add yourself
    me = "Me"
    for p in people:
        happiness.setdefault(p, {})[me] = 0
        happiness.setdefault(me, {})[p] = 0
    
    people.add(me)
    people = list(people)
    
    # Fix one person to remove rotational duplicates
    first = people[0]
    others = people[1:]
    
    best = float("-inf")
    
    for perm in itertools.permutations(others):
        seating = (first,) + perm
        total = 0
    
        for i in range(len(seating)):
            a = seating[i]
            b = seating[(i + 1) % len(seating)]
            total += happiness[a][b]
            total += happiness[b][a]
    
        best = max(best, total)
    
    print(best)
  ```

# This Concludes the Day 13 of Advent of Code
