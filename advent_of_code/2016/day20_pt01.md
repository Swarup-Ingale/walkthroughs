# URL
https://adventofcode.com/2016/day/20

# Description
You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:
```
5-8
0-2
4-7
```
The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    def lowest_allowed_ip(filename):
        ranges = []
    
        with open(filename, "r") as f:
            for line in f:
                start, end = map(int, line.strip().split("-"))
                ranges.append((start, end))
    
        ranges.sort()
    
        current = 0
    
        for start, end in ranges:
            if start > current:
                return current
            current = max(current, end + 1)
    
        return current
    
    
    result = lowest_allowed_ip("input_20")
    print("Lowest allowed IP:", result)
  ```
- This solves the part 01 of this challenge. 
