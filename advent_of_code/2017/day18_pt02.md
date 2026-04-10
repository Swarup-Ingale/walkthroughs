# URL
https://adventofcode.com/2017/day/18#part2

# Description
As you congratulate yourself for a job well done, you notice that the documentation has been on the back of the tablet this entire time. While you actually got most of the instructions correct, there are a few key differences. This assembly code isn't about sound at all - it's meant to be run twice at the same time.

Each running copy of the program has its own set of registers and follows the code independently - in fact, the programs don't even necessarily run at the same speed. To coordinate, they use the send (snd) and receive (rcv) instructions:

snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.

For example:
```
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
```
Both programs begin by sending three values to the other. Program 0 sends 1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and stores it in a, receives another value (both 2) and stores it in b, and then each receives the program ID of the other program (program 0 receives 1; program 1 receives 0) and stores it in c. Each program now sees a different value in its own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for either of them, and they reach a deadlock. When this happens, both programs terminate.

It should be noted that it would be equally valid for the programs to run at different speeds; for example, program 0 might have sent all three values and then stopped at the first rcv before program 1 executed even its first instruction.

Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?

# Method Of Solve
- The Part 02 of this challenge can be solved using the following code:
```
from collections import deque


def get_value(x, reg):
    if x.lstrip('-').isdigit():
        return int(x)
    return reg.get(x, 0)


def part2(instructions):
    reg0 = {'p': 0}
    reg1 = {'p': 1}

    q0 = deque()
    q1 = deque()

    i0 = i1 = 0
    send_count = 0

    while True:
        blocked0 = blocked1 = False

        # Program 0
        if 0 <= i0 < len(instructions):
            parts = instructions[i0].split()
            op = parts[0]

            if op == "snd":
                q1.append(get_value(parts[1], reg0))
            elif op == "set":
                reg0[parts[1]] = get_value(parts[2], reg0)
            elif op == "add":
                reg0[parts[1]] = reg0.get(parts[1], 0) + get_value(parts[2], reg0)
            elif op == "mul":
                reg0[parts[1]] = reg0.get(parts[1], 0) * get_value(parts[2], reg0)
            elif op == "mod":
                reg0[parts[1]] = reg0.get(parts[1], 0) % get_value(parts[2], reg0)
            elif op == "rcv":
                if q0:
                    reg0[parts[1]] = q0.popleft()
                else:
                    blocked0 = True
            elif op == "jgz":
                if get_value(parts[1], reg0) > 0:
                    i0 += get_value(parts[2], reg0)
                    continue

            if not blocked0:
                i0 += 1
        else:
            blocked0 = True

        # Program 1
        if 0 <= i1 < len(instructions):
            parts = instructions[i1].split()
            op = parts[0]

            if op == "snd":
                q0.append(get_value(parts[1], reg1))
                send_count += 1
            elif op == "set":
                reg1[parts[1]] = get_value(parts[2], reg1)
            elif op == "add":
                reg1[parts[1]] = reg1.get(parts[1], 0) + get_value(parts[2], reg1)
            elif op == "mul":
                reg1[parts[1]] = reg1.get(parts[1], 0) * get_value(parts[2], reg1)
            elif op == "mod":
                reg1[parts[1]] = reg1.get(parts[1], 0) % get_value(parts[2], reg1)
            elif op == "rcv":
                if q1:
                    reg1[parts[1]] = q1.popleft()
                else:
                    blocked1 = True
            elif op == "jgz":
                if get_value(parts[1], reg1) > 0:
                    i1 += get_value(parts[2], reg1)
                    continue

            if not blocked1:
                i1 += 1
        else:
            blocked1 = True

        # Deadlock condition
        if blocked0 and blocked1:
            return send_count


if __name__ == "__main__":
    with open("input_18", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]

    print("Program 1 send count:", part2(instructions))
```

# This Concludes Day 18 of The Advent of Code.
