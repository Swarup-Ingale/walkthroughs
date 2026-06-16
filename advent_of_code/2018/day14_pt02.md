# URL
adventofcode.com/2018/day/14#part2

# Description
As it turns out, you got the Elves' plan backwards. They actually want to know how many recipes appear on the scoreboard to the left of the first recipes whose scores are the digits from your puzzle input.
```
    51589 first appears after 9 recipes.
    01245 first appears after 5 recipes.
    92510 first appears after 18 recipes.
    59414 first appears after 2018 recipes.
```
How many recipes appear on the scoreboard to the left of the score sequence in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
target = list(
    map(
        int,
        open("input_14")
        .read()
        .strip()
    )
)

recipes = [3, 7]

e1 = 0
e2 = 1

while True:

    total = recipes[e1] + recipes[e2]

    for digit in map(int, str(total)):

        recipes.append(digit)

        if (
            recipes[-len(target):]
            == target
        ):
            print(
                len(recipes)
                - len(target)
            )
            raise SystemExit

    e1 = (
        e1 +
        recipes[e1] +
        1
    ) % len(recipes)

    e2 = (
        e2 +
        recipes[e2] +
        1
    ) % len(recipes)
```
- The Javascript version is as follows:
```
const fs = require('fs');

const target =
    fs.readFileSync('input_14', 'utf8')
      .trim()
      .split('')
      .map(Number);

const recipes = [3, 7];

let e1 = 0;
let e2 = 1;

function match(offset) {

    if (
        recipes.length - offset <
        target.length
    ) return false;

    for (let i = 0; i < target.length; i++) {

        if (
            recipes[
                recipes.length -
                target.length -
                offset + i
            ] !== target[i]
        ) {
            return false;
        }
    }

    return true;
}

while (true) {

    const sum =
        recipes[e1] +
        recipes[e2];

    if (sum >= 10) {

        recipes.push(1);

        if (match(0)) {
            console.log(
                recipes.length -
                target.length
            );
            break;
        }
    }

    recipes.push(sum % 10);

    if (match(0)) {
        console.log(
            recipes.length -
            target.length
        );
        break;
    }

    e1 =
        (e1 + recipes[e1] + 1)
        % recipes.length;

    e2 =
        (e2 + recipes[e2] + 1)
        % recipes.length;
}
```

# This Concludes Day 14 of The Advent of Code.
