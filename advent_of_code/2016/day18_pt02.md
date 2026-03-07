# URL
https://adventofcode.com/2016/day/18#part2

# Description
How many safe tiles are there in a total of 400000 rows?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def next_row(row):
        new_row = ""
    
        for i in range(len(row)):
            left = row[i-1] if i > 0 else "."
            center = row[i]
            right = row[i+1] if i < len(row)-1 else "."
    
            pattern = left + center + right
    
            if pattern in ["^^.", ".^^", "^..", "..^"]:
                new_row += "^"
            else:
                new_row += "."
    
        return new_row
    
    
    def count_safe_tiles(filename, rows=400000):
        with open(filename, "r") as f:
            row = f.read().strip()
    
        safe_count = row.count(".")
    
        for _ in range(rows - 1):
            row = next_row(row)
            safe_count += row.count(".")
    
        return safe_count
    
    
    result = count_safe_tiles("input_18", 400000)
    print("Safe tiles:", result)
  ```

# This Concludes Day 18 of The Advent of Code.
