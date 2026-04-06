# URL
https://adventofcode.com/2017/day/16#part2

# Description
Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:
```
s1, a spin of size 1: cbaed.
x3/4, swapping the last two programs: cbade.
pe/b, swapping programs e and b: ceadb.
```
In what order are the programs standing after their billion dances?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
```
def dance(programs, moves):
    programs = list(programs)

    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]

        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]

        elif move[0] == 'p':
            a, b = move[1:].split('/')
            ia = programs.index(a)
            ib = programs.index(b)
            programs[ia], programs[ib] = programs[ib], programs[ia]

    return ''.join(programs)


def part2(moves, iterations=1_000_000_000):
    seen = {}
    state = "abcdefghijklmnop"

    for i in range(iterations):
        if state in seen:
            cycle_start = seen[state]
            cycle_length = i - cycle_start

            remaining = (iterations - i) % cycle_length

            # jump directly
            for _ in range(remaining):
                state = dance(state, moves)

            return state

        seen[state] = i
        state = dance(state, moves)

    return state


if __name__ == "__main__":
    with open("input_16") as f:
        moves = f.read().strip().split(',')

    result = part2(moves)
    print(result)
```

# This Concludes Day 16 of The Advent of Code.
