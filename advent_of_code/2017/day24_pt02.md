# URL
https://adventofcode.com/2017/day/24#part2

# Description
The bridge you've built isn't long enough; you can't jump the rest of the way.

In the example above, there are two longest bridges:
```
0/2--2/2--2/3--3/4
0/2--2/2--2/3--3/5
```
Of them, the one which uses the 3/5 component is stronger; its strength is 0+2 + 2+2 + 2+3 + 3+5 = 19.

What is the strength of the longest bridge you can make? If you can make multiple bridges of the longest length, pick the strongest one.

# Method of Solve
- The Part 02 of this challenge can be solves using the following code:
```
def dfs(port, components, used):
    best_length = 0
    best_strength = 0

    for i, (a, b) in enumerate(components):
        if i in used:
            continue

        if a == port or b == port:
            used.add(i)

            next_port = b if a == port else a
            length, strength = dfs(next_port, components, used)

            length += 1
            strength += a + b

            if length > best_length or (length == best_length and strength > best_strength):
                best_length = length
                best_strength = strength

            used.remove(i)

    return best_length, best_strength


if __name__ == "__main__":
    components = []

    with open("input_24") as f:
        for line in f:
            a, b = map(int, line.strip().split('/'))
            components.append((a, b))

    length, strength = dfs(0, components, set())
    print("Longest bridge strength:", strength)
```

# This Concludes Day 24 of The Advent of Code.
