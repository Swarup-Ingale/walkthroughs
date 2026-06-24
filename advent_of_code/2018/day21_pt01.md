# URL
https://adventofcode.com/2018/day/21

# Description 
You should have been watching where you were going, because as you wander the new North Pole base, you trip and fall into a very deep hole!

Just kidding. You're falling through time again.

If you keep up your current pace, you should have resolved all of the temporal anomalies by the next time the device activates. Since you have very little interest in browsing history in 500-year increments for the rest of your life, you need to find a way to get back to your present time.

After a little research, you discover two important facts about the behavior of the device:

First, you discover that the device is hard-wired to always send you back in time in 500-year increments. Changing this is probably not feasible.

Second, you discover the activation system (your puzzle input) for the time travel module. Currently, it appears to run forever without halting.

If you can cause the activation system to halt at a specific moment, maybe you can make the device send you so far back in time that you cause an integer underflow in time itself and wrap around back to your current time!

The device executes the program as specified in manual section one and manual section two.

Your goal is to figure out how the program works and cause it to halt. You can only control register 0; every other register begins at 0 as usual.

Because time travel is a dangerous activity, the activation system begins with a few instructions which verify that bitwise AND (via bani) does a numeric operation and not an operation as if the inputs were interpreted as strings. If the test fails, it enters an infinite loop re-running the test instead of allowing the program to execute normally. If the test passes, the program continues, and assumes that all other bitwise operations (banr, bori, and borr) also interpret their inputs as numbers. (Clearly, the Elves who wrote this system were worried that someone might introduce a bug while trying to emulate this system with a scripting language.)

What is the lowest non-negative integer value for register 0 that causes the program to halt after executing the fewest instructions? (Executing the same instruction multiple times counts as multiple instructions executed.)

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
r2 = 0

while True:

    r1 = r2 | 65536
    r2 = 1250634

    while True:

        r2 += r1 & 255
        r2 &= 16777215

        r2 *= 65899
        r2 &= 16777215

        if r1 < 256:
            print(r2)
            raise SystemExit

        r1 //= 256
```
- The Javascript version is as follows:
```
let r2 = 0;

while (true) {

    let r1 = r2 | 65536;
    r2 = 1250634;

    while (true) {

        r2 += r1 & 255;
        r2 &= 16777215;

        r2 *= 65899;
        r2 &= 16777215;

        if (r1 < 256) {
            console.log(r2);
            process.exit(0);
        }

        r1 = Math.floor(r1 / 256);
    }
}
```
- This Solves Part 01 of this challenge.

# NOTE: The code depends on the input u have got .... so you first have to alter the code as per your input.
