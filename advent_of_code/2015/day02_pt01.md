# URL
https://adventofcode.com/2015/day/2

# Description
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:
```
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
```
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

# Concept
The challenge focuses on parsing input strings, performing basic arithmetic and comparisons, iterating over data, and applying logical problem decomposition using file I/O.

# Method of Solve
The code is used to solve the part 01 of the challenge:
```
  total = 0
  
  with open("input_02_01", "r") as file:
      for line in file:
          line = line.strip()
          if not line:
              continue
  
          l, w, h = map(int, line.split("x"))
  
          side1 = l * w
          side2 = w * h
          side3 = h * l
  
          surface_area = 2 * (side1 + side2 + side3)
          slack = min(side1, side2, side3)
  
          total += surface_area + slack
  
  print("Total wrapping paper required:", total)
```

# Hence Part 01 of the challenge is solved
