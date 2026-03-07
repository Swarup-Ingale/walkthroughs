# URL
https://adventofcode.com/2016/day/23

# Description
This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who wouldn't hide a star in a safe behind a painting?

The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see 7.

When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your prototype computer! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.

Now, you just need to figure out what output the keypad would have sent to the safe. You extract the assembunny code from the logic chip (your puzzle input).
The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

- For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
- For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
- The arguments of a toggled instruction are not affected.
- If an attempt is made to toggle an instruction outside the program, nothing happens.
- If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
- If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.
For example, given this program:
```
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
```
- cpy 2 a initializes register a to 2.
- The first tgl a toggles an instruction a (2) away from it, which changes the third tgl a into inc a.
- The second tgl a also modifies an instruction 2 away from it, which changes the cpy 1 a into jnz 1 a.
- The fourth line, which is now inc a, increments a to 3.
- Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions ahead, skipping the dec a instructions.
In this example, the final value in register a is 3.

The rest of the electronics seem to place the keypad entry (the number of eggs, 7) in register a, run the code, and then send the value left in register a to the safe.

What value should be sent to the safe?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    def get_value(x, registers):
        if x.lstrip("-").isdigit():
            return int(x)
        return registers[x]
    
    
    def run_program(filename, a_start=7):
        with open(filename) as f:
            program = [line.strip().split() for line in f]
    
        registers = {"a": a_start, "b": 0, "c": 0, "d": 0}
        i = 0
    
        while i < len(program):
            instr = program[i]
    
            if instr[0] == "cpy":
                x, y = instr[1], instr[2]
                if y in registers:
                    registers[y] = get_value(x, registers)
    
            elif instr[0] == "inc":
                registers[instr[1]] += 1
    
            elif instr[0] == "dec":
                registers[instr[1]] -= 1
    
            elif instr[0] == "jnz":
                x, y = instr[1], instr[2]
                if get_value(x, registers) != 0:
                    i += get_value(y, registers)
                    continue
    
            elif instr[0] == "tgl":
                x = get_value(instr[1], registers)
                target = i + x
    
                if 0 <= target < len(program):
                    t = program[target]
    
                    if len(t) == 2:
                        if t[0] == "inc":
                            t[0] = "dec"
                        else:
                            t[0] = "inc"
    
                    elif len(t) == 3:
                        if t[0] == "jnz":
                            t[0] = "cpy"
                        else:
                            t[0] = "jnz"
    
            i += 1
    
        return registers["a"]
    
    
    print("Part 1:", run_program("input_23", 7))
  ```
- This Solves the Part 01 of this challenge.
