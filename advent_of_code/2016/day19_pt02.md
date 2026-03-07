# URL
https://adventofcode.com/2016/day/19#part2

# Description
Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf directly across the circle. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced.

For example, with five Elves (again numbered 1 to 5):

- The Elves sit in a circle; Elf 1 goes first:
```
  1
5   2
 4 3
```
- Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one to the left. Elf 3 leaves the circle, and the rest of the Elves move in:
```
  1           1
5   2  -->  5   2
 4 -          4
```
- Elf 2 steals from the Elf directly across the circle, Elf 5:
```
  1         1 
-   2  -->     2
  4         4 
```
- Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:
```
 -          2  
    2  -->
 4          4
```
- Finally, Elf 2 steals from Elf 4:
```
 2
    -->  2  
 -
```
So, with five Elves, the Elf that sits starting in position 2 gets all the presents.

With the number of Elves given in your puzzle input, which Elf now gets all the presents?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    import math
    
    def winner_part2(filename):
        with open(filename, "r") as f:
            n = int(f.read().strip())
    
        p = 3 ** int(math.log(n, 3))
    
        if n == p:
            return n
        elif n <= 2 * p:
            return n - p
        else:
            return 2 * n - 3 * p
    
    
    result = winner_part2("input_19")
    print("Winning Elf:", result)
  ```

# This Concludes Day 19 of The Advent of Code.
