# URL
https://adventofcode.com/2017/day/14#part2

# Description
Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:
```
11.2.3..-->
.1.2.3.4   
....5.6.   
7.8.55.9   
.88.5...   
88..5..8   
.8...8..   
88.8.88.-->
|      |   
V      V
```
Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
def knot_hash(input_str):
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
    nums = list(range(256))
    pos = 0
    skip = 0

    for _ in range(64):
        for length in lengths:
            temp = []
            for i in range(length):
                temp.append(nums[(pos + i) % 256])
            temp.reverse()

            for i in range(length):
                nums[(pos + i) % 256] = temp[i]

            pos = (pos + length + skip) % 256
            skip += 1

    dense = []
    for i in range(0, 256, 16):
        x = nums[i]
        for j in range(1, 16):
            x ^= nums[i + j]
        dense.append(x)

    return ''.join(f"{x:02x}" for x in dense)


def count_used_squares(key):
    total = 0

    for i in range(128):
        row_hash = knot_hash(f"{key}-{i}")
        binary = bin(int(row_hash, 16))[2:].zfill(128)
        total += binary.count('1')

    return total


def build_grid(key):
    grid = []

    for i in range(128):
        row_hash = knot_hash(f"{key}-{i}")
        binary = bin(int(row_hash, 16))[2:].zfill(128)
        grid.append(list(binary))

    return grid


def dfs(grid, x, y):
    stack = [(x, y)]

    while stack:
        i, j = stack.pop()

        if i < 0 or j < 0 or i >= 128 or j >= 128:
            continue
        if grid[i][j] != '1':
            continue

        grid[i][j] = '0'

        stack.extend([
            (i+1, j), (i-1, j),
            (i, j+1), (i, j-1)
        ])


def count_regions(key):
    grid = build_grid(key)
    regions = 0

    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                regions += 1

    return regions


if __name__ == "__main__":
    key = input("Enter key: ").strip()

    print("Used Squares:", count_used_squares(key))
    print("Regions:", count_regions(key))
```

# This Concludes Day 14 of The Advent of Code.
