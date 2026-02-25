# URL
https://adventofcode.com/2016/day/8

# Description
You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:
```
rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
```
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:
```
###....
###....
.......
```
rotate column x=1 by 1 rotates the second column down by one pixel:
```
#.#....
###....
.#.....
```
rotate row y=0 by 4 rotates the top row right by four pixels:
```
....#.#
###....
.#.....
```
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:
```
.#..#.#
#.#....
.#.....
```
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    # Screen dimensions
    WIDTH = 50
    HEIGHT = 6
    
    # Create screen (all pixels OFF)
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
                parts = line.split()
                y = int(parts[2].split("=")[1])
                shift = int(parts[-1])
                screen[y] = screen[y][-shift:] + screen[y][:-shift]
    
            elif line.startswith("rotate column"):
                parts = line.split()
                x = int(parts[2].split("=")[1])
                shift = int(parts[-1])
    
                column = [screen[y][x] for y in range(HEIGHT)]
                column = column[-shift:] + column[:-shift]
    
                for y in range(HEIGHT):
                    screen[y][x] = column[y]
    
    # Count lit pixels
    lit_pixels = sum(sum(row) for row in screen)
    
    print("Number of lit pixels:", lit_pixels)
  ```
- This Solves the part 01 of the challenge.
