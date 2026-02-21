# URL
https://adventofcode.com/2016/day/3#part2

# Description
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    valid_count = 0
    
    with open("input_03", "r") as file:
        lines = file.read().splitlines()
    
    # Convert all lines into lists of integers
    rows = [list(map(int, line.split())) for line in lines]
    
    # Process input in chunks of 3 rows
    for i in range(0, len(rows), 3):
        row1 = rows[i]
        row2 = rows[i + 1]
        row3 = rows[i + 2]
    
        # Check triangles column-wise
        for col in range(3):
            sides = [row1[col], row2[col], row3[col]]
            sides.sort()
    
            if sides[0] + sides[1] > sides[2]:
                valid_count += 1
    
    print("Number of possible triangles:", valid_count)
  ```

# This Concludes the Day 03 of The Advent of Code.
