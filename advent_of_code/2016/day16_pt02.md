# URL
https://adventofcode.com/2016/day/16#part2

# Description
The second disk you have to fill has length 35651584. Again using the initial state in your puzzle input, what is the correct checksum for this disk?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def dragon_expand(data):
        b = data[::-1]
        b = ''.join('1' if c == '0' else '0' for c in b)
        return data + '0' + b
    
    
    def generate_data(initial, length):
        data = initial
        while len(data) < length:
            data = dragon_expand(data)
        return data[:length]
    
    
    def checksum(data):
        while len(data) % 2 == 0:
            data = ''.join(
                '1' if data[i] == data[i+1] else '0'
                for i in range(0, len(data), 2)
            )
        return data
    
    
    def solve(filename):
        with open(filename, "r") as f:
            initial = f.read().strip()
    
        disk_length = 35651584
    
        data = generate_data(initial, disk_length)
        return checksum(data)
    
    
    result = solve("input_16")
    print("Checksum:", result)
  ```

# This Concludes the Day 16 of The Advent of Code.
