# URL
https://adventofcode.com/2015/day/3

# Description
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:
```
> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
```

# Concept
This challenge uses grid traversal, coordinate tracking, sets for uniqueness, loops, and basic conditional logic.

# Method of Solve
The part 01 of this challenge can be solved by following code:
```
  visited = set()
  x, y = 0, 0
  
  visited.add((x, y))
  
  with open("input_03_01", "r") as file:
      directions = file.read().strip()
  
      for move in directions:
          if move == '^':
              y += 1
          elif move == 'v':
              y -= 1
          elif move == '>':
              x += 1
          elif move == '<':
              x -= 1
  
          visited.add((x, y))
  
  print("Houses that received at least one present:", len(visited))
```

# This is how the part 01 is solved
