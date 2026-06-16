# URL
https://adventofcode.com/2018/day/15#part2

# Description
According to your calculations, the Elves are going to lose badly. Surely, you won't mess up the timeline too much if you give them just a little advanced technology, right?

You need to make sure the Elves not only win, but also suffer no losses: even the death of a single Elf is unacceptable.

However, you can't go too far: larger changes will be more likely to permanently alter spacetime.

So, you need to find the outcome of the battle in which the Elves have the lowest integer attack power (at least 4) that allows them to win without a single death. The Goblins always have an attack power of 3.

In the first summarized example above, the lowest attack power the Elves need to win without losses is 15:
```
#######       #######
#.G...#       #..E..#   E(158)
#...EG#       #...E.#   E(14)
#.#.#G#  -->  #.#.#.#
#..G#E#       #...#.#
#.....#       #.....#
#######       #######
```
Combat ends after 29 full rounds
Elves win with 172 total hit points left
Outcome: 29 * 172 = 4988

In the second example above, the Elves need only 4 attack power:
```
#######       #######
#E..EG#       #.E.E.#   E(200), E(23)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##E#   E(125), E(200)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#
#######       #######
```
Combat ends after 33 full rounds
Elves win with 948 total hit points left
Outcome: 33 * 948 = 31284

In the third example above, the Elves need 15 attack power:
```
#######       #######
#E.G#.#       #.E.#.#   E(8)
#.#G..#       #.#E..#   E(86)
#G.#.G#  -->  #..#..#
#G..#.#       #...#.#
#...E.#       #.....#
#######       #######
```
Combat ends after 37 full rounds
Elves win with 94 total hit points left
Outcome: 37 * 94 = 3478

In the fourth example above, the Elves need 12 attack power:
```
#######       #######
#.E...#       #...E.#   E(14)
#.#..G#       #.#..E#   E(152)
#.###.#  -->  #.###.#
#E#G#G#       #.#.#.#
#...#G#       #...#.#
#######       #######
```
Combat ends after 39 full rounds
Elves win with 166 total hit points left
Outcome: 39 * 166 = 6474

In the last example above, the lone Elf needs 34 attack power:
```
#########       #########   
#G......#       #.......#   
#.E.#...#       #.E.#...#   E(38)
#..##..G#       #..##...#   
#...##..#  -->  #...##..#   
#...#...#       #...#...#   
#.G...G.#       #.......#   
#.....G.#       #.......#   
#########       #########   
```
Combat ends after 30 full rounds
Elves win with 38 total hit points left
Outcome: 30 * 38 = 1140

After increasing the Elves' attack power until it is just barely enough for them to win without any Elves dying, what is the outcome of the combat described in your puzzle input?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows :
```
from collections import deque
from copy import deepcopy

raw = [list(line.rstrip()) for line in open("input_15")]

dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def simulate(elf_attack):

    grid = deepcopy(raw)
    units = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in "GE":
                units.append({
                    "x": x,
                    "y": y,
                    "type": grid[y][x],
                    "hp": 200,
                    "atk": elf_attack if grid[y][x] == "E" else 3,
                    "alive": True
                })
                grid[y][x] = "."

    elves_start = sum(u["type"] == "E" for u in units)

    def occupied(x, y):
        return any(
            u["alive"] and
            u["x"] == x and
            u["y"] == y
            for u in units
        )

    def adjacent(unit):
        enemies = [
            u for u in units
            if u["alive"]
            and u["type"] != unit["type"]
            and abs(u["x"] - unit["x"]) + abs(u["y"] - unit["y"]) == 1
        ]

        enemies.sort(
            key=lambda u: (
                u["hp"],
                u["y"],
                u["x"]
            )
        )

        return enemies

    def bfs(unit):

        enemies = [
            u for u in units
            if u["alive"]
            and u["type"] != unit["type"]
        ]

        targets = set()

        for e in enemies:
            for dx, dy in dirs:
                nx = e["x"] + dx
                ny = e["y"] + dy

                if (
                    0 <= ny < len(grid)
                    and 0 <= nx < len(grid[0])
                    and grid[ny][nx] == "."
                    and not occupied(nx, ny)
                ):
                    targets.add((nx, ny))

        if not targets:
            return None

        q = deque([
            (unit["x"], unit["y"], 0, None)
        ])

        visited = {
            (unit["x"], unit["y"])
        }

        found = []

        while q:

            x, y, dist, first = q.popleft()

            if found and dist > found[0][2]:
                break

            if (x, y) in targets:
                found.append(
                    (x, y, dist, first)
                )
                continue

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if (
                    not (0 <= ny < len(grid))
                    or not (0 <= nx < len(grid[0]))
                ):
                    continue

                if (
                    (nx, ny) in visited
                    or grid[ny][nx] != "."
                    or occupied(nx, ny)
                ):
                    continue

                visited.add((nx, ny))

                q.append(
                    (
                        nx,
                        ny,
                        dist + 1,
                        first or (nx, ny)
                    )
                )

        if not found:
            return None

        found.sort(
            key=lambda p: (
                p[1],
                p[0]
            )
        )

        return found[0][3]

    rounds = 0

    while True:

        units.sort(
            key=lambda u: (
                u["y"],
                u["x"]
            )
        )

        for unit in units:

            if not unit["alive"]:
                continue

            enemies = [
                u for u in units
                if u["alive"]
                and u["type"] != unit["type"]
            ]

            if not enemies:

                elves_alive = sum(
                    u["alive"] and u["type"] == "E"
                    for u in units
                )

                if elves_alive != elves_start:
                    return None

                hp = sum(
                    u["hp"]
                    for u in units
                    if u["alive"]
                )

                return rounds * hp

            if not adjacent(unit):

                move = bfs(unit)

                if move:
                    unit["x"], unit["y"] = move

            targets = adjacent(unit)

            if targets:

                victim = targets[0]

                victim["hp"] -= unit["atk"]

                if victim["hp"] <= 0:

                    victim["alive"] = False

                    if victim["type"] == "E":
                        return None

        rounds += 1


attack = 4

while True:

    result = simulate(attack)

    if result is not None:
        print(result)
        break

    attack += 1
```
- The Javascript version is as follows :
```
const fs = require('fs');

const original = fs.readFileSync('input_15', 'utf8')
    .trimEnd()
    .split('\n')
    .map(r => r.split(''));

const dirs = [
    [0, -1],
    [-1, 0],
    [1, 0],
    [0, 1]
];

function simulate(elfAttack) {

    const grid = original.map(r => [...r]);
    const units = [];

    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {

            if ('GE'.includes(grid[y][x])) {

                units.push({
                    x,
                    y,
                    type: grid[y][x],
                    hp: 200,
                    atk: grid[y][x] === 'E' ? elfAttack : 3,
                    alive: true
                });

                grid[y][x] = '.';
            }
        }
    }

    const elvesStart =
        units.filter(u => u.type === 'E').length;

    const occupied = (x, y) =>
        units.some(u =>
            u.alive &&
            u.x === x &&
            u.y === y
        );

    function adjacent(unit) {

        return units
            .filter(u =>
                u.alive &&
                u.type !== unit.type &&
                Math.abs(u.x - unit.x) +
                Math.abs(u.y - unit.y) === 1
            )
            .sort((a, b) =>
                a.hp - b.hp ||
                a.y - b.y ||
                a.x - b.x
            );
    }

    function bfs(unit) {

        const enemies =
            units.filter(u =>
                u.alive &&
                u.type !== unit.type
            );

        const targets = new Set();

        for (const e of enemies) {

            for (const [dx, dy] of dirs) {

                const nx = e.x + dx;
                const ny = e.y + dy;

                if (
                    grid[ny]?.[nx] === '.' &&
                    !occupied(nx, ny)
                ) {
                    targets.add(`${nx},${ny}`);
                }
            }
        }

        if (!targets.size) return null;

        const visited =
            new Set([`${unit.x},${unit.y}`]);

        const q = [{
            x: unit.x,
            y: unit.y,
            dist: 0,
            first: null
        }];

        const found = [];

        while (q.length) {

            const cur = q.shift();

            if (
                found.length &&
                cur.dist > found[0].dist
            ) break;

            const key =
                `${cur.x},${cur.y}`;

            if (targets.has(key)) {
                found.push(cur);
                continue;
            }

            for (const [dx, dy] of dirs) {

                const nx = cur.x + dx;
                const ny = cur.y + dy;
                const nk = `${nx},${ny}`;

                if (
                    visited.has(nk) ||
                    grid[ny]?.[nx] !== '.' ||
                    occupied(nx, ny)
                ) continue;

                visited.add(nk);

                q.push({
                    x: nx,
                    y: ny,
                    dist: cur.dist + 1,
                    first: cur.first || [nx, ny]
                });
            }
        }

        if (!found.length) return null;

        found.sort((a, b) =>
            a.y - b.y ||
            a.x - b.x
        );

        return found[0].first;
    }

    let rounds = 0;

    while (true) {

        units.sort((a, b) =>
            a.y - b.y ||
            a.x - b.x
        );

        for (const unit of units) {

            if (!unit.alive) continue;

            const enemies =
                units.filter(u =>
                    u.alive &&
                    u.type !== unit.type
                );

            if (!enemies.length) {

                const elvesAlive =
                    units.filter(
                        u => u.alive &&
                        u.type === 'E'
                    ).length;

                if (elvesAlive !== elvesStart)
                    return null;

                const hp =
                    units
                        .filter(u => u.alive)
                        .reduce(
                            (s, u) => s + u.hp,
                            0
                        );

                return rounds * hp;
            }

            if (!adjacent(unit).length) {

                const move = bfs(unit);

                if (move) {
                    unit.x = move[0];
                    unit.y = move[1];
                }
            }

            const targets =
                adjacent(unit);

            if (targets.length) {

                const victim =
                    targets[0];

                victim.hp -= unit.atk;

                if (victim.hp <= 0) {

                    victim.alive = false;

                    if (
                        victim.type === 'E'
                    ) {
                        return null;
                    }
                }
            }
        }

        rounds++;
    }
}

let attack = 4;

while (true) {

    const result =
        simulate(attack);

    if (result !== null) {
        console.log(result);
        break;
    }

    attack++;
}
```

# This Concludes Day 15 of The Advent of Code.
