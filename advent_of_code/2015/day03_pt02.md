# URL
https://adventofcode.com/2015/day/3#part2

# Description
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:
```
^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
```

# Concept
The Challenge extends grid traversal by managing multiple agents, alternating state updates, and tracking shared visited positions using a set.

# Method of Solve
The code given below solves the challenge for part 02:
```
  visited = set()
  
  sx, sy = 0, 0
  rx, ry = 0, 0
  
  visited.add((0, 0))
  
  with open("input_03_01", "r") as file:
      directions = file.read().strip()
  
      for i, move in enumerate(directions):
          if i % 2 == 0:  		# Santa's turn
              if move == '^':
                  sy += 1
              elif move == 'v':
                  sy -= 1
              elif move == '>':
                  sx += 1
              elif move == '<':
                  sx -= 1
  
              visited.add((sx, sy))
  
          else:  				# Robo-Santa's turn
              if move == '^':
                  ry += 1
              elif move == 'v':
                  ry -= 1
              elif move == '>':
                  rx += 1
              elif move == '<':
                  rx -= 1
  
              visited.add((rx, ry))
  
  print("Houses that received at least one present:", len(visited))
```

# This concludes the solution of Day 03 of the advent of code
