# URL
https://adventofcode.com/2016/day/25

# Description
You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.

However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

Nothing happens.

You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.

"No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter Bunny installation, and you're definitely not-" You hang up the phone.

You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly compatible with code you worked on just recently.

This antenna code, being a signal generator, uses one extra instruction:

out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.

What is the lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever?

# Method of Solve
- The Part 01 of the final day can be solved using the following code:
  ```
    def get_value(x, r):
        if x.lstrip("-").isdigit():
            return int(x)
        return r[x]
    
    
    def run(program, a_value, limit=100):
        r = {"a": a_value, "b": 0, "c": 0, "d": 0}
        i = 0
        output = []
    
        while 0 <= i < len(program) and len(output) < limit:
            ins = program[i]
    
            if ins[0] == "cpy":
                x, y = ins[1], ins[2]
                if y in r:
                    r[y] = get_value(x, r)
    
            elif ins[0] == "inc":
                r[ins[1]] += 1
    
            elif ins[0] == "dec":
                r[ins[1]] -= 1
    
            elif ins[0] == "jnz":
                x, y = ins[1], ins[2]
                if get_value(x, r) != 0:
                    i += get_value(y, r)
                    continue
    
            elif ins[0] == "out":
                val = get_value(ins[1], r)
    
                if val not in (0, 1):
                    return False
    
                if output and output[-1] == val:
                    return False
    
                output.append(val)
    
            i += 1
    
        return len(output) == limit
    
    
    def find_clock_signal(filename):
        with open(filename) as f:
            program = [line.split() for line in f]
    
        a = 0
        while True:
            if run(program, a):
                return a
            a += 1
    
    
    print("Part 1:", find_clock_signal("input_25"))
  ```
- This Solves the part 01 of the challenge.
