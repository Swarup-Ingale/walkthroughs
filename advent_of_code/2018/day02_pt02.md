# URL
https://adventofcode.com/2018/day/2#part2

# Description
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:
```
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
```
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input_02") as f:
    ids = [line.strip() for line in f]

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        differences = 0
        common = []

        for a, b in zip(ids[i], ids[j]):
            if a == b:
                common.append(a)
            else:
                differences += 1

        if differences == 1:
            print("".join(common))
            exit()
```
- The Javascript version is as follows :
```
const fs = require('fs');

const ids = fs
    .readFileSync('input_02', 'utf8')
    .trim()
    .split('\n');

for (let i = 0; i < ids.length; i++) {
    for (let j = i + 1; j < ids.length; j++) {

        let diff = 0;
        let common = '';

        for (let k = 0; k < ids[i].length; k++) {
            if (ids[i][k] === ids[j][k]) {
                common += ids[i][k];
            } else {
                diff++;
            }
        }

        if (diff === 1) {
            console.log(common);
            process.exit(0);
        }
    }
}
```

# This Concludes The Day 02 of The Advent of Code.
