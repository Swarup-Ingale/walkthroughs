# URL
https://adventofcode.com/2016/day/21#part2

# Description
You scrambled the password correctly, but you discover that you can't actually modify the password file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.

What is the un-scrambled version of the scrambled password fbgdceah?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from itertools import permutations
    from day21_pt01 import scramble
    target = "fbgdceah"
    
    for p in permutations("abcdefgh"):
        candidate = "".join(p)
        if scramble("input_21", candidate) == target:
            print("Original password:", candidate)
            break
  ```

# This Concludes Day 21 of The Advent of Code.
