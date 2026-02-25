# URL
https://adventofcode.com/2016/day/8#part2

# Description
You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    # Screen dimensions
    WIDTH = 50
    HEIGHT = 6
    
    # Initialize screen (0 = off, 1 = on)
    screen = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    with open("input_08", "r") as f:
        for line in f:
            line = line.strip()
    
            if line.startswith("rect"):
                A, B = map(int, line.split()[1].split("x"))
                for y in range(B):
                    for x in range(A):
                        screen[y][x] = 1
    
            elif line.startswith("rotate row"):
                y = int(line.split()[2].split("=")[1])
                shift = int(line.split()[-1])
                screen[y] = screen[y][-shift:] + screen[y][:-shift]
    
            elif line.startswith("rotate column"):
                x = int(line.split()[2].split("=")[1])
                shift = int(line.split()[-1])
    
                column = [screen[y][x] for y in range(HEIGHT)]
                column = column[-shift:] + column[:-shift]
    
                for y in range(HEIGHT):
                    screen[y][x] = column[y]
    
    # Print final screen
    print("\nFinal screen output:\n")
    for row in screen:
        print("".join("#" if pixel else "." for pixel in row))
  ```
# This Concludes the Day 08 of The Advent of Code.
