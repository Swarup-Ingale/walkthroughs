# URL
https://adventofcode.com/2016/day/17#part2

# Description 
You're curious how robust this security solution really is, and so you decide to find longer and longer paths which still provide access to the vault. You remember that paths always end the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).

For example:
```
If your passcode were ihgpwlah, the longest path would take 370 steps.
With kglvqrro, the longest path would be 492 steps long.
With ulqzkmiv, the longest path would be 830 steps long.
```
What is the length of the longest path that reaches the vault?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    import hashlib
    from collections import deque
    
    
    def get_open_doors(passcode, path):
        h = hashlib.md5((passcode + path).encode()).hexdigest()
        doors = []
    
        if h[0] in "bcdef":
            doors.append("U")
        if h[1] in "bcdef":
            doors.append("D")
        if h[2] in "bcdef":
            doors.append("L")
        if h[3] in "bcdef":
            doors.append("R")
    
        return doors
    
    
    def longest_path(filename):
        with open(filename, "r") as f:
            passcode = f.read().strip()
    
        queue = deque([(0, 0, "")])
        longest = 0
    
        while queue:
            x, y, path = queue.popleft()
    
            # reached vault
            if (x, y) == (3, 3):
                longest = max(longest, len(path))
                continue
    
            for move in get_open_doors(passcode, path):
                nx, ny = x, y
    
                if move == "U":
                    ny -= 1
                elif move == "D":
                    ny += 1
                elif move == "L":
                    nx -= 1
                elif move == "R":
                    nx += 1
    
                if 0 <= nx < 4 and 0 <= ny < 4:
                    queue.append((nx, ny, path + move))
    
        return longest
    
    
    result = longest_path("input_17")
    print("Longest path length:", result)
  ```

# This Concludes Day 17 of The Advent of Code.
