# URL
https://adventofcode.com/2017/day/21#part2

# Description
How many pixels stay on after 18 iterations?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
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

    for _ in range(18):
        grid = enhance(grid, rules)

    print("Pixels ON:", count_on(grid))
```

# This Concludes Day 21 of The Advent Of Code.
