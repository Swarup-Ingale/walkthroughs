# URL
https://adventofcode.com/2018/day/11#part2

# Description
You discover a dial on the side of the device; it seems to let you select a square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total power. Identify this square by including its size as a third parameter after the top-left coordinate: a 9x9 square with a top-left corner of 3,5 is identified as 3,5,9.

For example:
```
    For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
    For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.
```
What is the X,Y,size identifier of the square with the largest total power?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
- The python version is as follows:
```
SERIAL = int(open("input_11").read().strip())

SIZE = 300

sat = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]

for y in range(1, SIZE + 1):
    row_sum = 0

    for x in range(1, SIZE + 1):

        rack = x + 10

        power = rack * y
        power += SERIAL
        power *= rack

        power = (power // 100) % 10
        power -= 5

        row_sum += power

        sat[y][x] = sat[y - 1][x] + row_sum


def square_sum(x, y, s):

    x2 = x + s - 1
    y2 = y + s - 1

    return (
        sat[y2][x2]
        - sat[y - 1][x2]
        - sat[y2][x - 1]
        + sat[y - 1][x - 1]
    )


best = float("-inf")
answer = None

for size in range(1, 301):

    for y in range(1, 302 - size):
        for x in range(1, 302 - size):

            total = square_sum(x, y, size)

            if total > best:
                best = total
                answer = (x, y, size)

print(f"{answer[0]},{answer[1]},{answer[2]}")
```
- The Javascript version is as follows:
```
const fs = require('fs');

const SERIAL = Number(
    fs.readFileSync('input_11', 'utf8').trim()
);

const SIZE = 300;

const sat = Array.from(
    { length: SIZE + 1 },
    () => Array(SIZE + 1).fill(0)
);

for (let y = 1; y <= SIZE; y++) {

    let rowSum = 0;

    for (let x = 1; x <= SIZE; x++) {

        const rack = x + 10;

        let power = rack * y;
        power += SERIAL;
        power *= rack;

        power = Math.floor(power / 100) % 10;
        power -= 5;

        rowSum += power;

        sat[y][x] =
            sat[y - 1][x] + rowSum;
    }
}

function squareSum(x, y, s) {

    const x2 = x + s - 1;
    const y2 = y + s - 1;

    return (
        sat[y2][x2]
        - sat[y - 1][x2]
        - sat[y2][x - 1]
        + sat[y - 1][x - 1]
    );
}

let best = -Infinity;
let answer = null;

for (let size = 1; size <= 300; size++) {

    for (let y = 1; y <= 301 - size; y++) {
        for (let x = 1; x <= 301 - size; x++) {

            const total =
                squareSum(x, y, size);

            if (total > best) {
                best = total;
                answer = [x, y, size];
            }
        }
    }
}

console.log(answer.join(','));
```

# This Concludes Day 11 of The Advent of Code.
