# URL
https://adventofcode.com/2015/day/15#part2

# Description
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

# Method of Solve
- The Solution for the Part 02 of the Challenge can be given by following code:
  ```
    import re

    ingredients = []
    
    with open("input_15_01") as f:
        for line in f:
            nums = list(map(int, re.findall(r"-?\d+", line)))
            ingredients.append(nums)
            # [capacity, durability, flavor, texture, calories]
    
    best = 0
    
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                amounts = [a, b, c, d]
    
                calories = 0
                for i in range(4):
                    calories += ingredients[i][4] * amounts[i]
    
                if calories != 500:
                    continue
    
                totals = [0, 0, 0, 0]
                for i in range(4):
                    for p in range(4):
                        totals[p] += ingredients[i][p] * amounts[i]
    
                score = 1
                for t in totals:
                    score *= max(0, t)
    
                best = max(best, score)
    
    print(best)
  ```

# This Concludes the Day 15 of The Advent of Code
