# URL
https://adventofcode.com/2016/day/9#part2

# Description
Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are decompressed. This, the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to be stored in only a few kilobytes.

For example:
```
(3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
(27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
```
Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.

What is the decompressed length of the file using this improved format?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    def decompressed_length_v2(data):
        i = 0
        total_length = 0
    
        while i < len(data):
            if data[i] == '(':
                end = data.index(')', i)
                A, B = map(int, data[i+1:end].split('x'))
    
                # Substring affected by marker
                segment = data[end + 1 : end + 1 + A]
    
                # Recursively compute its length
                segment_length = decompressed_length_v2(segment)
    
                total_length += segment_length * B
                i = end + 1 + A
            else:
                total_length += 1
                i += 1
    
        return total_length
    
    
    # Read input and remove whitespace
    with open("input_09", "r") as f:
        compressed = "".join(f.read().split())
    
    result = decompressed_length_v2(compressed)
    print("Decompressed length (Part 2):", result)
  ```

# This Concludes the Day 09 of The Advent of Code.
