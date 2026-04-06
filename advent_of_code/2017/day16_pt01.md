# URL
https://adventofcode.com/2017/day/16

# Description 
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:
```
Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
```
For example, with only five programs standing in a line (abcde), they could do the following dance:
```
s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.
```

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

# Method of Solve
- The Part 01 of this challenge can eb solved using the following code:
```
def dance(programs, moves):
    programs = list(programs)

    for move in moves:
        if move[0] == 's':  # spin
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]

        elif move[0] == 'x':  # exchange by position
            a, b = map(int, move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]

        elif move[0] == 'p':  # partner by name
            a, b = move[1:].split('/')
            for i in range(len(programs)):
                if programs[i] == a:
                    ia = i
                if programs[i] == b:
                    ib = i
            programs[ia], programs[ib] = programs[ib], programs[ia]

    return ''.join(programs)


if __name__ == "__main__":
    with open("input_16") as f:
        moves = f.read().strip().split(',')

    print("Final order:", dance("abcdefghijklmnop", moves))
```
- This Solves the Part 01 of this challenge.
