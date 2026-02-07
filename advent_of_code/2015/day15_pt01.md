# URL
https://adventofcode.com/2015/day/15

# Description
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:
```
capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
```
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:
```
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
```
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

# Method of Solve
- The part 01 of the challenge can be solved using the following code:
  ```
    import re
    import itertools
    
    ingredients = []
    
    with open("input_15_01") as f:
        for line in f:
            nums = list(map(int, re.findall(r"-?\d+", line)))
            ingredients.append(nums)  
            # order: capacity, durability, flavor, texture, calories
    
    best = 0
    
    # 4 ingredients → a + b + c + d = 100
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                amounts = [a, b, c, d]
    
                totals = [0, 0, 0, 0]
                for i in range(4):
                    for p in range(4):  # ignore calories
                        totals[p] += ingredients[i][p] * amounts[i]
    
                score = 1
                for t in totals:
                    score *= max(0, t)
    
                best = max(best, score)
    
    print(best)
  ```

# This Solves the part 01 of the challenge
