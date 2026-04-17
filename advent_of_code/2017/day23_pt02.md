# URL
https://adventofcode.com/2017/day/23#part2

# Description
Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch, which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program obviously didn't choose a very efficient implementation. You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. Technically, if it had that... it wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion, what value would be left in register h?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    b = 109300
    c = 126300
    step = 17

    h = 0

    for x in range(b, c + 1, step):
        if not is_prime(x):
            h += 1

    print("Value of h:", h)
```
- Note : The Values of b, c and steps are found using proper reverse engineering on the puzzle input ... so the values might differ from person to person.

# This Concludes Day 23 of The Advent of Code.
