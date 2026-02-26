# URL
https://adventofcode.com/2016/day/11#part2

# Description
You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:
```
An elerium generator.
An elerium-compatible microchip.
A dilithium generator.
A dilithium-compatible microchip.
```
These work just like the other generators and microchips. You'll have to get them up to assembly as well.

What is the minimum number of steps required to bring all of the objects, including these four new ones, to the fourth floor?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    import re
    from collections import deque
    from itertools import combinations
    
    # Safety Check
    def is_safe(pairs):
        gens = {g for _, g in pairs}
        for chip, gen in pairs:
            if chip != gen and chip in gens:
                return False
        return True
    
    # Normalize State 
    def normalize(elevator, pairs):
        return (elevator, tuple(sorted(pairs)))
    
    # Solver
    def solve(initial_pairs):
        start = normalize(0, initial_pairs)
        queue = deque([(start, 0)])
        visited = {start}
    
        while queue:
            (elevator, pairs), steps = queue.popleft()
    
            # Goal: everything on floor 3 (4th floor)
            if all(c == 3 and g == 3 for c, g in pairs):
                return steps
    
            # Items on current floor
            items = []
            for i, (c, g) in enumerate(pairs):
                if c == elevator:
                    items.append((i, 0))  # chip
                if g == elevator:
                    items.append((i, 1))  # generator
    
            # Try moving 1 or 2 items
            for move in list(combinations(items, 1)) + list(combinations(items, 2)):
                for direction in (-1, 1):
                    new_floor = elevator + direction
                    if not (0 <= new_floor < 4):
                        continue
    
                    # Small optimization: don't move down if nothing is below
                    if direction == -1:
                        if not any(
                            c < elevator or g < elevator
                            for c, g in pairs
                        ):
                            continue
    
                    new_pairs = list(pairs)
                    for idx, typ in move:
                        c, g = new_pairs[idx]
                        if typ == 0:
                            new_pairs[idx] = (new_floor, g)
                        else:
                            new_pairs[idx] = (c, new_floor)
    
                    if not is_safe(new_pairs):
                        continue
    
                    state = normalize(new_floor, new_pairs)
                    if state not in visited:
                        visited.add(state)
                        queue.append((state, steps + 1))
    
    # Input Parser 
    def parse_input(filename):
        element_map = {}
        floors = []
    
        with open(filename, "r") as f:
            for floor, line in enumerate(f):
                chips = re.findall(r"(\w+)-compatible microchip", line)
                gens = re.findall(r"(\w+) generator", line)
                floors.append((chips, gens))
    
        for chips, gens in floors:
            for e in chips + gens:
                if e not in element_map:
                    element_map[e] = [None, None]
    
        for floor, (chips, gens) in enumerate(floors):
            for c in chips:
                element_map[c][0] = floor
            for g in gens:
                element_map[g][1] = floor
    
        return [tuple(v) for v in element_map.values()]
    
    pairs = parse_input("input_11")
    
    # Add extra Part 2 items on floor 0
    pairs.extend([
        (0, 0),  # elerium chip & generator
        (0, 0),  # dilithium chip & generator
    ])
    
    result = solve(pairs)
    print("Minimum number of steps (Part 2):", result)
  ```

# This Concludes the Day 11 of The Advent of Code.
