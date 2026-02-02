# URL
https://adventofcode.com/2015/day/6#part2

# Description
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:
```
turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
```

# Method of Solve
This Challenge can be solved using the code given below:
  ```
    grid = [[0] * 1000 for _ in range(1000)]

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
                    if cmd == "on":
                        grid[x][y] += 1
                    elif cmd == "off":
                        grid[x][y] = max(0, grid[x][y] - 1)
                    else:
                        grid[x][y] += 2
    
    print(sum(sum(row) for row in grid))
  ```
This Solves the day 06 of Advent of Code
