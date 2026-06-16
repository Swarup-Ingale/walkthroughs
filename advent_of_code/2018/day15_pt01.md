# URL
https://adventofcode.com/2018/day/15

# Description
Having perfected their hot chocolate, the Elves have a new problem: the Goblins that live in these caves will do anything to steal it. Looks like they're here for a fight.

You scan the area, generating a map of the walls (#), open cavern (.), and starting position of every Goblin (G) and Elf (E) (your puzzle input).

Combat proceeds in rounds; in each round, each unit that is still alive takes a turn, resolving all of its actions before the next unit's turn begins. On each unit's turn, it tries to move into range of an enemy (if it isn't already) and then attack (if it is in range).

All units are very disciplined and always follow very strict combat rules. Units never move or attack diagonally, as doing so would be dishonorable. When multiple choices are equally valid, ties are broken in reading order: top-to-bottom, then left-to-right. For instance, the order in which units take their turns within a round is the reading order of their starting positions in that round, regardless of the type of unit or whether other units have moved after the round started. For example:
```
                 would take their
These units:   turns in this order:
  #######           #######
  #.G.E.#           #.1.2.#
  #E.G.E#           #3.4.5#
  #.G.E.#           #.6.7.#
  #######           #######
```
Each unit begins its turn by identifying all possible targets (enemy units). If no targets remain, combat ends.

Then, the unit identifies all of the open squares (.) that are in range of each target; these are the squares which are adjacent (immediately up, down, left, or right) to any target and which aren't already occupied by a wall or another unit. Alternatively, the unit might already be in range of a target. If the unit is not already in range of a target, and there are no open squares which are in range of a target, the unit ends its turn.

If the unit is already in range of a target, it does not move, but continues its turn with an attack. Otherwise, since it is not in range of a target, it moves.

To move, the unit first considers the squares that are in range and determines which of those squares it could reach in the fewest steps. A step is a single movement to any adjacent (immediately up, down, left, or right) open (.) square. Units cannot move into walls or other units. The unit does this while considering the current positions of units and does not do any prediction about where units will be later. If the unit cannot reach (find an open path to) any of the squares that are in range, it ends its turn. If multiple squares are in range and tied for being reachable in the fewest steps, the square which is first in reading order is chosen. For example:
```
Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######
```
In the above scenario, the Elf has three targets (the three Goblins):

    Each of the Goblins has open, adjacent squares which are in range (marked with a ? on the map).
    Of those squares, four are reachable (marked @); the other two (on the right) would require moving through a wall or unit to reach.
    Three of these reachable squares are nearest, requiring the fewest steps (only 2) to reach (marked !).
    Of those, the square which is first in reading order is chosen (+).

The unit then takes a single step toward the chosen square along the shortest path to that square. If multiple steps would put the unit equally closer to its destination, the unit chooses the step which is first in reading order. (This requires knowing when there is more than one shortest path so that you can consider the first step of each such path.) For example:
```
In range:     Nearest:      Chosen:       Distance:     Step:
#######       #######       #######       #######       #######
#.E...#       #.E...#       #.E...#       #4E212#       #..E..#
#...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
#..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
#######       #######       #######       #######       #######
```
The Elf sees three squares in range of a target (?), two of which are nearest (!), and so the first in reading order is chosen (+). Under "Distance", each open square is marked with its distance from the destination square; the two squares to which the Elf could move on this turn (down and to the right) are both equally good moves and would leave the Elf 2 steps from being in range of the Goblin. Because the step which is first in reading order is chosen, the Elf moves right one square.

Here's a larger example of movement:
```
Initially:
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########

After 1 round:
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########

After 2 rounds:
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########

After 3 rounds:
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########
```
Once the Goblins and Elf reach the positions above, they all are either in range of a target or cannot find any square in range of a target, and so none of the units can move until a unit dies.

After moving (or if the unit began its turn in range of a target), the unit attacks.

To attack, the unit first determines all of the targets that are in range of it by being immediately adjacent to it. If there are no such targets, the unit ends its turn. Otherwise, the adjacent target with the fewest hit points is selected; in a tie, the adjacent target with the fewest hit points which is first in reading order is selected.

The unit deals damage equal to its attack power to the selected target, reducing its hit points by that amount. If this reduces its hit points to 0 or fewer, the selected target dies: its square becomes . and it takes no further turns.

Each unit, either Goblin or Elf, has 3 attack power and starts with 200 hit points.

For example, suppose the only Elf is about to attack:
```
       HP:            HP:
G....  9       G....  9  
..G..  4       ..G..  4  
..EG.  2  -->  ..E..     
..G..  2       ..G..  2  
...G.  1       ...G.  1  
```
The "HP" column shows the hit points of the Goblin to the left in the corresponding row. The Elf is in range of three targets: the Goblin above it (with 4 hit points), the Goblin to its right (with 2 hit points), and the Goblin below it (also with 2 hit points). Because three targets are in range, the ones with the lowest hit points are selected: the two Goblins with 2 hit points each (one to the right of the Elf and one below the Elf). Of those, the Goblin first in reading order (the one to the right of the Elf) is selected. The selected Goblin's hit points (2) are reduced by the Elf's attack power (3), reducing its hit points to -1, killing it.

After attacking, the unit's turn ends. Regardless of how the unit's turn ends, the next unit in the round takes its turn. If all units have taken turns in this round, the round ends, and a new round begins.

The Elves look quite outnumbered. You need to determine the outcome of the battle: the number of full rounds that were completed (not counting the round in which combat ends) multiplied by the sum of the hit points of all remaining units at the moment combat ends. (Combat only ends when a unit finds no targets during its turn.)

Below is an entire sample combat. Next to each map, each row's units' hit points are listed from left to right.
```
Initially:
#######   
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#   
#######   

After 1 round:
#######   
#..G..#   G(200)
#...EG#   E(197), G(197)
#.#G#G#   G(200), G(197)
#...#E#   E(197)
#.....#   
#######   

After 2 rounds:
#######   
#...G.#   G(200)
#..GEG#   G(200), E(188), G(194)
#.#.#G#   G(194)
#...#E#   E(194)
#.....#   
#######   

Combat ensues; eventually, the top Elf dies:

After 23 rounds:
#######   
#...G.#   G(200)
#..G.G#   G(200), G(131)
#.#.#G#   G(131)
#...#E#   E(131)
#.....#   
#######   

After 24 rounds:
#######   
#..G..#   G(200)
#...G.#   G(131)
#.#G#G#   G(200), G(128)
#...#E#   E(128)
#.....#   
#######   

After 25 rounds:
#######   
#.G...#   G(200)
#..G..#   G(131)
#.#.#G#   G(125)
#..G#E#   G(200), E(125)
#.....#   
#######   

After 26 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(122)
#...#E#   E(122)
#..G..#   G(200)
#######   

After 27 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(119)
#...#E#   E(119)
#...G.#   G(200)
#######   

After 28 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(116)
#...#E#   E(113)
#....G#   G(200)
#######   

More combat ensues; eventually, the bottom Elf dies:

After 47 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(59)
#...#.#   
#....G#   G(200)
#######   
```
Before the 48th round can finish, the top-left Goblin finds that there are no targets remaining, and so combat ends. So, the number of full rounds that were completed is 47, and the sum of the hit points of all remaining units is 200+131+59+200 = 590. From these, the outcome of the battle is 47 * 590 = 27730.

Here are a few example summarized combats:
```
#######       #######
#G..#E#       #...#E#   E(200)
#E#E.E#       #E#...#   E(197)
#G.##.#  -->  #.E##.#   E(185)
#...#E#       #E..#E#   E(200), E(200)
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 982 total hit points left
Outcome: 37 * 982 = 36334

#######       #######   
#E..EG#       #.E.E.#   E(164), E(197)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##.#   E(98)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#   
#######       #######   

Combat ends after 46 full rounds
Elves win with 859 total hit points left
Outcome: 46 * 859 = 39514

#######       #######   
#E.G#.#       #G.G#.#   G(200), G(98)
#.#G..#       #.#G..#   G(200)
#G.#.G#  -->  #..#..#   
#G..#.#       #...#G#   G(95)
#...E.#       #...G.#   G(200)
#######       #######   

Combat ends after 35 full rounds
Goblins win with 793 total hit points left
Outcome: 35 * 793 = 27755

#######       #######   
#.E...#       #.....#   
#.#..G#       #.#G..#   G(200)
#.###.#  -->  #.###.#   
#E#G#G#       #.#.#.#   
#...#G#       #G.G#G#   G(98), G(38), G(200)
#######       #######   

Combat ends after 54 full rounds
Goblins win with 536 total hit points left
Outcome: 54 * 536 = 28944

#########       #########   
#G......#       #.G.....#   G(137)
#.E.#...#       #G.G#...#   G(200), G(200)
#..##..G#       #.G##...#   G(200)
#...##..#  -->  #...##..#   
#...#...#       #.G.#...#   G(200)
#.G...G.#       #.......#   
#.....G.#       #.......#   
#########       #########   
```
Combat ends after 20 full rounds
Goblins win with 937 total hit points left
Outcome: 20 * 937 = 18740

What is the outcome of the combat described in your puzzle input?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
from collections import deque

grid = [list(line.rstrip('\n')) for line in open('input_15')]

units = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in 'GE':
            units.append({
                'x': x,
                'y': y,
                'type': grid[y][x],
                'hp': 200,
                'atk': 3,
                'alive': True
            })
            grid[y][x] = '.'

dirs = [
    (0, -1),   # up
    (-1, 0),   # left
    (1, 0),    # right
    (0, 1)     # down
]

def occupied(x, y):
    return any(
        u['alive'] and
        u['x'] == x and
        u['y'] == y
        for u in units
    )

def adjacent_enemies(unit):
    enemies = [
        u for u in units
        if u['alive']
        and u['type'] != unit['type']
        and abs(u['x'] - unit['x']) + abs(u['y'] - unit['y']) == 1
    ]

    enemies.sort(
        key=lambda u: (
            u['hp'],
            u['y'],
            u['x']
        )
    )

    return enemies

def bfs(unit):

    enemies = [
        u for u in units
        if u['alive']
        and u['type'] != unit['type']
    ]

    targets = set()

    for e in enemies:
        for dx, dy in dirs:

            nx = e['x'] + dx
            ny = e['y'] + dy

            if (
                0 <= ny < len(grid)
                and 0 <= nx < len(grid[0])
                and grid[ny][nx] == '.'
                and not occupied(nx, ny)
            ):
                targets.add((nx, ny))

    if not targets:
        return None

    visited = {(unit['x'], unit['y'])}

    q = deque([
        (
            unit['x'],
            unit['y'],
            0,
            None
        )
    ])

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
                or grid[ny][nx] != '.'
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
            u['y'],
            u['x']
        )
    )

    for unit in units:

        if not unit['alive']:
            continue

        enemies = [
            u for u in units
            if u['alive']
            and u['type'] != unit['type']
        ]

        if not enemies:

            hp = sum(
                u['hp']
                for u in units
                if u['alive']
            )

            print(rounds * hp)
            raise SystemExit

        if not adjacent_enemies(unit):

            move = bfs(unit)

            if move:
                unit['x'], unit['y'] = move

        targets = adjacent_enemies(unit)

        if targets:

            victim = targets[0]

            victim['hp'] -= unit['atk']

            if victim['hp'] <= 0:
                victim['alive'] = False

    rounds += 1
```
- The Javascript version is as follows :
```
const fs = require('fs');

const grid = fs.readFileSync('input_15', 'utf8')
    .trimEnd()
    .split('\n')
    .map(r => r.split(''));

const units = [];

for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[y].length; x++) {
        if ('GE'.includes(grid[y][x])) {
            units.push({
                x, y,
                type: grid[y][x],
                hp: 200,
                atk: 3,
                alive: true
            });
            grid[y][x] = '.';
        }
    }
}

const dirs = [
    [0, -1], // up
    [-1, 0], // left
    [1, 0], // right
    [0, 1] // down
];

function key(x, y) {
    return `${x},${y}`;
}

function occupied(x, y) {
    return units.some(u =>
        u.alive &&
        u.x === x &&
        u.y === y
    );
}

function adjacentEnemies(unit) {
    return units
        .filter(u =>
            u.alive &&
            u.type !== unit.type &&
            Math.abs(u.x - unit.x) + Math.abs(u.y - unit.y) === 1
        )
        .sort((a, b) =>
            a.hp - b.hp ||
            a.y - b.y ||
            a.x - b.x
        );
}

function bfs(unit) {

    const enemies = units.filter(
        u => u.alive && u.type !== unit.type
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
                targets.add(key(nx, ny));
            }
        }
    }

    if (!targets.size) return null;

    const visited = new Set([key(unit.x, unit.y)]);
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

        if (
            targets.has(key(cur.x, cur.y))
        ) {
            found.push(cur);
            continue;
        }

        for (const [dx, dy] of dirs) {

            const nx = cur.x + dx;
            const ny = cur.y + dy;
            const k = key(nx, ny);

            if (
                visited.has(k) ||
                grid[ny]?.[nx] !== '.' ||
                occupied(nx, ny)
            ) continue;

            visited.add(k);

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

        const enemies = units.filter(
            u => u.alive && u.type !== unit.type
        );

        if (!enemies.length) {

            const hp = units
                .filter(u => u.alive)
                .reduce((s, u) => s + u.hp, 0);

            console.log(rounds * hp);
            process.exit(0);
        }

        if (!adjacentEnemies(unit).length) {

            const move = bfs(unit);

            if (move) {
                unit.x = move[0];
                unit.y = move[1];
            }
        }

        const targets = adjacentEnemies(unit);

        if (targets.length) {

            const victim = targets[0];

            victim.hp -= unit.atk;

            if (victim.hp <= 0) {
                victim.alive = false;
            }
        }
    }

    rounds++;
}
```
- This Solves the Part 01 of this challenge.
