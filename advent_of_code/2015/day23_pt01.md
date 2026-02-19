# URL
https://adventofcode.com/2015/day/23

# Description
Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:
```
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
```
All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:
```
inc a
jio a, +2
tpl a
inc a
```
What is the value in register b when the program in your puzzle input is finished executing?

# Method of Solve
- The given challenge can be solved using the following code:
  ```
    def run_program(instructions):
        a, b = 0, 0
        ip = 0  # instruction pointer
    
        while 0 <= ip < len(instructions):
            inst = instructions[ip].replace(",", "").split()
    
            if inst[0] == "hlf":
                if inst[1] == "a":
                    a //= 2
                else:
                    b //= 2
                ip += 1
    
            elif inst[0] == "tpl":
                if inst[1] == "a":
                    a *= 3
                else:
                    b *= 3
                ip += 1
    
            elif inst[0] == "inc":
                if inst[1] == "a":
                    a += 1
                else:
                    b += 1
                ip += 1
    
            elif inst[0] == "jmp":
                ip += int(inst[1])
    
            elif inst[0] == "jie":
                r = a if inst[1] == "a" else b
                if r % 2 == 0:
                    ip += int(inst[2])
                else:
                    ip += 1
    
            elif inst[0] == "jio":
                r = a if inst[1] == "a" else b
                if r == 1:
                    ip += int(inst[2])
                else:
                    ip += 1
    
        return b
    
    
    # LOAD YOUR PUZZLE INPUT
    with open("input_23_01") as f:
        instructions = [line.strip() for line in f]
    
    print("Value in register b:", run_program(instructions))
  ```
- This Solves the Part 01 of the challenge.
