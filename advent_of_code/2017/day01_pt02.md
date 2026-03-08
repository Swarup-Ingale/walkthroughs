# URL
https://adventofcode.com/2017/day/1#part2

# Description
You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:
```
1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
```
What is the solution to your new captcha?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    def captcha_sum(filename):
        with open(filename, "r") as file:
            digits = file.read().strip()
    
        total = 0
        n = len(digits)
        step = n // 2
    
        for i in range(n):
            if digits[i] == digits[(i + step) % n]:
                total += int(digits[i])
    
        return total
    
    
    result = captcha_sum("input_01")
    print("Captcha Solution (Part 2):", result)
  ```

# This Concludes Day 01 of The Advent of Code.
