# URL
https://adventofcode.com/2015/day/6

# Description
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:
```
turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
```
After following the instructions, how many lights are lit?

# Method of Solve
The below code is solution for solving the challenge:
```
  grid = [[False] * 1000 for _ in range(1000)]

  with open("input_06_01") as f:
      for line in f:
          line = line.strip()
  
          if line.startswith("turn on"):
              cmd = "on"
              line = line[8:]
          elif line.startswith("turn off"):
              cmd = "off"
              line = line[9:]
          else:  
              cmd = "toggle"
              line = line[7:]
  
          start, _, end = line.split()
          x1, y1 = map(int, start.split(","))
          x2, y2 = map(int, end.split(","))
  
          for x in range(x1, x2 + 1):
              for y in range(y1, y2 + 1):
                  if cmd == "on":			# on
                      grid[x][y] = True
                  elif cmd == "off":		# off
                      grid[x][y] = False
                  else: 				# toggle
                      grid[x][y] = not grid[x][y]
  
    # Count lights that are ON
    print(sum(sum(row) for row in grid))
  ```

# This solves the part 01 of the challenge
