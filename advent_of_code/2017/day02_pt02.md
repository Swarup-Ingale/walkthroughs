# URL
https://adventofcode.com/2017/day/2#part2

# Description
"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:
```
5 9 2 8
9 4 7 3
3 8 6 5
```
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    def checksum(filename):
        total = 0
    
        with open(filename, "r") as file:
            for line in file:
                numbers = list(map(int, line.split()))
    
                for i in numbers:
                    for j in numbers:
                        if i != j and i % j == 0:
                            total += i // j
                            break
    
        return total
    
    
    result = checksum("input_02")
    print("Checksum Part 2:", result)
  ```

# This Concludes Day 02 of Advent of Code.
