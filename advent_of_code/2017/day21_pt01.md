# URL
https://adventofcode.com/2017/day/21

# Description
You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:
```
.#.
..#
###
```
Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:
```
../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.
```
When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:
```
.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.
```
Suppose the book contained the following two rules:
```
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
```
As before, the program begins with this pattern:
```
.#.
..#
###
```
The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:
```
#..#
....
....
#..#
```
The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:
```
#.|.#
..|..
--+--
..|..
#.|.#
```
Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:
```
##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...
```
Finally, the squares are joined into a new grid:
```
##.##.
#..#..
......
##.##.
#..#..
......
```
Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

# Method of Solve
- The part 01 of this challenge can be solved using the following code:
```
def rotate(grid):
    return [''.join(row[i] for row in reversed(grid)) for i in range(len(grid))]

def flip(grid):
    return [row[::-1] for row in grid]

def variations(grid):
    grids = []
    for _ in range(4):
        grid = rotate(grid)
        grids.append(grid)
        grids.append(flip(grid))
    return grids

def parse_rules(filename):
    rules = {}
    with open(filename) as f:
        for line in f:
            inp, out = line.strip().split(" => ")
            inp = inp.split('/')
            out = out.split('/')

            for v in variations(inp):
                rules[tuple(v)] = out
    return rules

def split_grid(grid):
    size = len(grid)
    block = 2 if size % 2 == 0 else 3
    chunks = []

    for i in range(0, size, block):
        row = []
        for j in range(0, size, block):
            sub = [grid[i+k][j:j+block] for k in range(block)]
            row.append(sub)
        chunks.append(row)

    return chunks

def merge_grid(chunks):
    new_grid = []

    for row in chunks:
        for i in range(len(row[0])):
            new_row = ""
            for block in row:
                new_row += block[i]
            new_grid.append(new_row)

    return new_grid

def enhance(grid, rules):
    chunks = split_grid(grid)

    for i in range(len(chunks)):
        for j in range(len(chunks[i])):
            chunks[i][j] = rules[tuple(chunks[i][j])]

    return merge_grid(chunks)

def count_on(grid):
    return sum(row.count('#') for row in grid)


if __name__ == "__main__":
    rules = parse_rules("input_21")

    grid = [
        ".#.",
        "..#",
        "###"
    ]

    for _ in range(5):
        grid = enhance(grid, rules)

    print("Pixels ON:", count_on(grid))
```
- This solves the Part 01 of this challenge.
