# URL
https://adventofcode.com/2015/day/20#part2

# Description
The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    puzzle_input = int(input("Enter the number of presents: "))

    limit = puzzle_input // 11
    houses = [0] * (limit + 1)
    
    for elf in range(1, limit + 1):
        for house in range(elf, min(elf * 50 + 1, limit + 1), elf):
            houses[house] += elf * 11
    
    for house_number, presents in enumerate(houses):
        if presents >= puzzle_input:
            print("Lowest house number:", house_number)
            break
  ```

# This Concludes the Day 20 of The Advent of Code.
