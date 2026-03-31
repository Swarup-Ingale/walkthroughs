# URL
https://adventofcode.com/2017/day/14

# Description 
Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:
```
##.#.#..-->
.#.#.#.#   
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V
```
In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

# Method of Solve 
- The Part 01 of this challenge can be solved using the following code:
```
def knot_hash(input_str):
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
    nums = list(range(256))
    pos = 0
    skip = 0

    for _ in range(64):
        for length in lengths:
            # reverse section
            temp = []
            for i in range(length):
                temp.append(nums[(pos + i) % 256])
            temp.reverse()

            for i in range(length):
                nums[(pos + i) % 256] = temp[i]

            pos = (pos + length + skip) % 256
            skip += 1

    # dense hash
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


if __name__ == "__main__":
    key = input("Enter key: ").strip()
    print("Used Squares:", count_used_squares(key))
```
- This Solves the Part 01 of this challenge.
