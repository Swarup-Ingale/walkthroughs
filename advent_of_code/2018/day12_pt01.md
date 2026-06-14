# URL
https://adventofcode.com/2018/day/12

# Description
The year 518 is significantly more underground than your history books implied. Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of small pots as far as you can see to your left and right. A few of them contain plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are numbered -1, -2, -3, and so on; to the right, 1, 2, 3.... Your puzzle input contains a list of pots from 0 to the right and whether they do (#) or do not (.) currently contain a plant, the initial state. (No other pots currently contain plants.) For example, an initial state of #..##.... indicates that pots 0, 3, and 4 currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone has been trying to figure out how these plants spread to nearby pots. Based on the notes, for each generation of plants, a given pot has or does not have a plant based on whether that pot (and the two pots on either side of it) had a plant in the last generation. These are written as LLCRR => N, where L are pots to the left, C is the current pot being considered, R are the pots to the right, and N is whether the current pot will have a plant in the next generation. For example:
```
    A note like ..#.. => . means that a pot that contains a plant but with no plants within two pots of it will not have a plant in it during the next generation.
    A note like ##.## => . means that an empty pot with two plants on each side of it will remain empty in the next generation.
    A note like .##.# => # means that a pot has a plant in a given generation if, in the previous generation, there were plants in that pot, the one immediately to the left, and the one two pots to the right, but not in the ones immediately to the right and two to the left.
```
It's not clear what these plants are for, but you're sure it's important, so you'd like to make sure the current configuration of plants is sustainable by determining what will happen after 20 generations.

For example, given the following input:

initial state: #..#.#..##......###...###
```
...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
```
For brevity, in this example, only the combinations which do produce a plant are listed. (Your input includes all possible combinations.) Then, the next 20 generations will look like this:
```
                 1         2         3     
       0         0         0         0     
 0: ...#..#.#..##......###...###...........
 1: ...#...#....#.....#..#..#..#...........
 2: ...##..##...##....#..#..#..##..........
 3: ..#.#...#..#.#....#..#..#...#..........
 4: ...#.#..#...#.#...#..#..##..##.........
 5: ....#...##...#.#..#..#...#...#.........
 6: ....##.#.#....#...#..##..##..##........
 7: ...#..###.#...##..#...#...#...#........
 8: ...#....##.#.#.#..##..##..##..##.......
 9: ...##..#..#####....#...#...#...#.......
10: ..#.#..#...#.##....##..##..##..##......
11: ...#...##...#.#...#.#...#...#...#......
12: ...##.#.#....#.#...#.#..##..##..##.....
13: ..#..###.#....#.#...#....#...#...#.....
14: ..#....##.#....#.#..##...##..##..##....
15: ..##..#..#.#....#....#..#.#...#...#....
16: .#.#..#...#.#...##...#...#.#..##..##...
17: ..#...##...#.#.#.#...##...#....#...#...
18: ..##.#.#....#####.#.#.#...##...##..##..
19: .#..###.#..#.#.#######.#.#.#..#.#...#..
20: .#....##....#####...#######....#.#..##.
```
The generation is shown along the left, where 0 is the initial state. The pot numbers are shown along the top, where 0 labels the center pot, negative-numbered pots extend to the left, and positive pots extend toward the right. Remember, the initial state begins at pot 0, which is not the leftmost pot used in this example.

After one generation, only seven plants remain. The one in pot 0 matched the rule looking for ..#.., the one in pot 4 matched the rule looking for .#.#., pot 9 matched .##.., and so on.

In this example, after 20 generations, the pots shown as # contain plants, the furthest left of which is pot -2, and the furthest right of which is pot 34. Adding up all the numbers of plant-containing pots after the 20th generation produces 325.

After 20 generations, what is the sum of the numbers of all pots which contain a plant?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows :
```
with open("input_12") as f:
    lines = [line.strip() for line in f]

state = lines[0].split(": ")[1]

rules = {}

for line in lines[2:]:
    if line:
        pattern, result = line.split(" => ")
        rules[pattern] = result

plants = {
    i
    for i, c in enumerate(state)
    if c == "#"
}

for _ in range(20):

    new_plants = set()

    left = min(plants) - 2
    right = max(plants) + 2

    for pos in range(left, right + 1):

        pattern = ""

        for offset in range(-2, 3):
            pattern += (
                "#"
                if pos + offset in plants
                else "."
            )

        if rules.get(pattern) == "#":
            new_plants.add(pos)

    plants = new_plants

print(sum(plants))
```
- The Javascript version of the code is as follows:
```
const fs = require('fs');

const lines = fs
    .readFileSync('input_12', 'utf8')
    .trim()
    .split('\n');

const state =
    lines[0].split(': ')[1];

const rules = {};

for (const line of lines.slice(2)) {

    if (!line) continue;

    const [pattern, result] =
        line.split(' => ');

    rules[pattern] = result;
}

let plants = new Set();

for (let i = 0; i < state.length; i++) {

    if (state[i] === '#') {
        plants.add(i);
    }
}

for (let gen = 0; gen < 20; gen++) {

    const next = new Set();

    const values =
        [...plants];

    const min =
        Math.min(...values);

    const max =
        Math.max(...values);

    for (
        let pos = min - 2;
        pos <= max + 2;
        pos++
    ) {

        let pattern = '';

        for (
            let d = -2;
            d <= 2;
            d++
        ) {

            pattern +=
                plants.has(pos + d)
                    ? '#'
                    : '.';
        }

        if (
            rules[pattern] === '#'
        ) {
            next.add(pos);
        }
    }

    plants = next;
}

console.log(
    [...plants]
        .reduce(
            (a, b) => a + b,
            0
        )
);
```
- This Solves the Part 01 of this challenge.
