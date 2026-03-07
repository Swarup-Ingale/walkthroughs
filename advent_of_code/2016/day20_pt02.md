# URL
https://adventofcode.com/2016/day/20#part2

# Description
How many IPs are allowed by the blacklist?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def count_allowed_ips(filename):
        ranges = []
    
        with open(filename, "r") as f:
            for line in f:
                start, end = map(int, line.strip().split("-"))
                ranges.append((start, end))
    
        ranges.sort()
    
        current = 0
        allowed = 0
    
        for start, end in ranges:
            if start > current:
                allowed += start - current
            current = max(current, end + 1)
    
        MAX_IP = 4294967295
    
        if current <= MAX_IP:
            allowed += MAX_IP - current + 1
    
        return allowed
    
    
    result = count_allowed_ips("input_20")
    print("Total allowed IPs:", result)
  ```

# This Concludes Day 20 of The Advent of Code.
