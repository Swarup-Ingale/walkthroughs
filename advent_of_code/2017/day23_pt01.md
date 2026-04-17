# URL
https://adventofcode.com/2017/day/23

# Description
You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:
```
set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.
```
The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
```
def get_val(x, reg):
    if x.lstrip('-').isdigit():
        return int(x)
    return reg.get(x, 0)


if __name__ == "__main__":
    with open("input_23") as f:
        instructions = [line.strip().split() for line in f]

    reg = {}
    i = 0
    mul_count = 0

    while 0 <= i < len(instructions):
        op, *args = instructions[i]

        if op == "set":
            reg[args[0]] = get_val(args[1], reg)

        elif op == "sub":
            reg[args[0]] = reg.get(args[0], 0) - get_val(args[1], reg)

        elif op == "mul":
            reg[args[0]] = reg.get(args[0], 0) * get_val(args[1], reg)
            mul_count += 1

        elif op == "jnz":
            if get_val(args[0], reg) != 0:
                i += get_val(args[1], reg)
                continue

        i += 1

    print("mul count:", mul_count)
```
- This Solves the Part 01 of this challenge.
