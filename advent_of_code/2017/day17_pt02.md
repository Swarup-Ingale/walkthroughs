# URL
https://adventofcode.com/2017/day/17#part2

# Description
The spinlock does not short-circuit. Instead, it gets more angry. At least, you assume that's what happened; it's spinning significantly faster than it was a moment ago.

You have good news and bad news.

The good news is that you have improved calculations for how to stop the spinlock. They indicate that you actually need to identify the value after 0 in the current state of the circular buffer.

The bad news is that while you were determining this, the spinlock has just finished inserting its fifty millionth value (50000000).

What is the value after 0 the moment 50000000 is inserted?

# Method of Solve
- The Part 02 of this challenge can be solves using the following code:
```
def spinlock_fast(step, n=50_000_000):
    pos = 0
    value_after_0 = 0

    for i in range(1, n + 1):
        pos = (pos + step) % i + 1

        if pos == 1:
            value_after_0 = i

    return value_after_0


if __name__ == "__main__":
    step = int(input("Step size: "))
    print("Value after 0:", spinlock_fast(step))
```

# This Concludes Day 17 of The Advent of Code.
