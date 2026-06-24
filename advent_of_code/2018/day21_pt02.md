# URL
https://adventofcode.com/2018/day/21#part2

# Description
In order to determine the timing window for your underflow exploit, you also need an upper bound:

What is the lowest non-negative integer value for register 0 that causes the program to halt after executing the most instructions? (The program must actually halt; running forever does not count as halting.)

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
seen = set()

last = None
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

            if r2 in seen:
                print(last)
                raise SystemExit

            seen.add(r2)
            last = r2
            break

        r1 //= 256
```
- The Javascript version is as follows:
```
const seen = new Set();

let last = null;
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

            if (seen.has(r2)) {
                console.log(last);
                process.exit(0);
            }

            seen.add(r2);
            last = r2;
            break;
        }

        r1 = Math.floor(r1 / 256);
    }
}
```

# This Concludes Day 21 of The Advent of Code.
