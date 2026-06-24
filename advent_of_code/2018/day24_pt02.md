# URL
https://adventofcode.com/2018/day/24#part2

# Description
Things aren't looking good for the reindeer. The man asks whether more milk and cookies would help you think.

If only you could give the reindeer's immune system a boost, you might be able to change the outcome of the combat.

A boost is an integer increase in immune system units' attack damage. For example, if you were to boost the above example's immune system's units by 1570, the armies would instead look like this:
```
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with
 an attack that does 6077 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
 slashing) with an attack that does 1595 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack
 that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire,
 cold) with an attack that does 12 slashing damage at initiative 4
```
With this boost, the combat proceeds differently:
```
Immune System:
Group 2 contains 989 units
Group 1 contains 17 units
Infection:
Group 1 contains 801 units
Group 2 contains 4485 units

Infection group 1 would deal defending group 2 185832 damage
Infection group 1 would deal defending group 1 185832 damage
Infection group 2 would deal defending group 1 53820 damage
Immune System group 2 would deal defending group 1 1577455 damage
Immune System group 2 would deal defending group 2 1577455 damage
Immune System group 1 would deal defending group 2 206618 damage

Infection group 2 attacks defending group 1, killing 9 units
Immune System group 2 attacks defending group 1, killing 335 units
Immune System group 1 attacks defending group 2, killing 32 units
Infection group 1 attacks defending group 2, killing 84 units

Immune System:
Group 2 contains 905 units
Group 1 contains 8 units
Infection:
Group 1 contains 466 units
Group 2 contains 4453 units

Infection group 1 would deal defending group 2 108112 damage
Infection group 1 would deal defending group 1 108112 damage
Infection group 2 would deal defending group 1 53436 damage
Immune System group 2 would deal defending group 1 1443475 damage
Immune System group 2 would deal defending group 2 1443475 damage
Immune System group 1 would deal defending group 2 97232 damage

Infection group 2 attacks defending group 1, killing 8 units
Immune System group 2 attacks defending group 1, killing 306 units
Infection group 1 attacks defending group 2, killing 29 units

Immune System:
Group 2 contains 876 units
Infection:
Group 2 contains 4453 units
Group 1 contains 160 units

Infection group 2 would deal defending group 2 106872 damage
Immune System group 2 would deal defending group 2 1397220 damage
Immune System group 2 would deal defending group 1 1397220 damage

Infection group 2 attacks defending group 2, killing 83 units
Immune System group 2 attacks defending group 2, killing 427 units

After a few fights...

Immune System:
Group 2 contains 64 units
Infection:
Group 2 contains 214 units
Group 1 contains 19 units

Infection group 2 would deal defending group 2 5136 damage
Immune System group 2 would deal defending group 2 102080 damage
Immune System group 2 would deal defending group 1 102080 damage

Infection group 2 attacks defending group 2, killing 4 units
Immune System group 2 attacks defending group 2, killing 32 units

Immune System:
Group 2 contains 60 units
Infection:
Group 1 contains 19 units
Group 2 contains 182 units

Infection group 1 would deal defending group 2 4408 damage
Immune System group 2 would deal defending group 1 95700 damage
Immune System group 2 would deal defending group 2 95700 damage

Immune System group 2 attacks defending group 1, killing 19 units

Immune System:
Group 2 contains 60 units
Infection:
Group 2 contains 182 units

Infection group 2 would deal defending group 2 4368 damage
Immune System group 2 would deal defending group 2 95700 damage

Infection group 2 attacks defending group 2, killing 3 units
Immune System group 2 attacks defending group 2, killing 30 units

After a few more fights...

Immune System:
Group 2 contains 51 units
Infection:
Group 2 contains 40 units

Infection group 2 would deal defending group 2 960 damage
Immune System group 2 would deal defending group 2 81345 damage

Infection group 2 attacks defending group 2, killing 0 units
Immune System group 2 attacks defending group 2, killing 27 units

Immune System:
Group 2 contains 51 units
Infection:
Group 2 contains 13 units

Infection group 2 would deal defending group 2 312 damage
Immune System group 2 would deal defending group 2 81345 damage

Infection group 2 attacks defending group 2, killing 0 units
Immune System group 2 attacks defending group 2, killing 13 units

Immune System:
Group 2 contains 51 units
Infection:
No groups remain.
```
This boost would allow the immune system's armies to win! It would be left with 51 units.

You don't even know how you could boost the reindeer's immune system or what effect it might have, so you need to be cautious and find the smallest boost that would allow the immune system to win.

How many units does the immune system have left after getting the smallest boost it needs to win?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re
from copy import deepcopy

groups = []

army = None

for line in open("input_24"):

    line = line.strip()

    if not line:
        continue

    if line.endswith(":"):
        army = line[:-1]
        continue

    nums = list(map(int, re.findall(r"\d+", line)))

    units = nums[0]
    hp = nums[1]
    damage = nums[-2]
    initiative = nums[-1]

    attack = re.search(
        r"(\w+) damage",
        line
    ).group(1)

    weak = set()
    immune = set()

    m = re.search(r"\((.*?)\)", line)

    if m:

        for part in m.group(1).split(";"):

            part = part.strip()

            if part.startswith("weak to"):
                weak.update(
                    x.strip()
                    for x in
                    part[8:].split(",")
                )

            elif part.startswith("immune to"):
                immune.update(
                    x.strip()
                    for x in
                    part[10:].split(",")
                )

    groups.append({
        "id": len(groups),
        "army": army,
        "units": units,
        "hp": hp,
        "damage": damage,
        "type": attack,
        "initiative": initiative,
        "weak": weak,
        "immune": immune
    })


def simulate(boost=0):

    g = deepcopy(groups)

    for x in g:
        if x["army"] == "Immune System":
            x["damage"] += boost

    while True:

        alive = [
            x for x in g
            if x["units"] > 0
        ]

        armies = {
            x["army"]
            for x in alive
        }

        if len(armies) == 1:

            return (
                alive[0]["army"],
                sum(
                    x["units"]
                    for x in alive
                )
            )

        targets = {}
        chosen = set()

        order = sorted(
            alive,
            key=lambda x: (
                -(x["units"] * x["damage"]),
                -x["initiative"]
            )
        )

        for a in order:

            best = None

            for b in alive:

                if (
                    a["army"] == b["army"] or
                    b["id"] in chosen
                ):
                    continue

                damage = (
                    a["units"] *
                    a["damage"]
                )

                if a["type"] in b["immune"]:
                    damage = 0

                elif a["type"] in b["weak"]:
                    damage *= 2

                if damage == 0:
                    continue

                score = (
                    damage,
                    b["units"] * b["damage"],
                    b["initiative"]
                )

                if (
                    best is None or
                    score > best[0]
                ):
                    best = (score, b)

            if best:
                targets[a["id"]] = best[1]
                chosen.add(best[1]["id"])

        attack_order = sorted(
            alive,
            key=lambda x: -x["initiative"]
        )

        killed = 0

        for a in attack_order:

            if a["units"] <= 0:
                continue

            if a["id"] not in targets:
                continue

            b = targets[a["id"]]

            if b["units"] <= 0:
                continue

            damage = (
                a["units"] *
                a["damage"]
            )

            if a["type"] in b["immune"]:
                damage = 0

            elif a["type"] in b["weak"]:
                damage *= 2

            dead = min(
                b["units"],
                damage // b["hp"]
            )

            b["units"] -= dead
            killed += dead

        if killed == 0:
            return None, 0


winner, units = simulate()

print("Part 1:", units)

boost = 1

while True:

    winner, units = simulate(boost)

    if winner == "Immune System":
        print("Part 2:", units)
        break

    boost += 1
```
- The Javascript version is as follows:
```
const fs = require('fs');

const lines = fs.readFileSync('input_24', 'utf8')
    .trim()
    .split('\n');

const groups = [];

let army = null;

for (const line of lines) {

    if (!line.trim())
        continue;

    if (line.endsWith(':')) {
        army = line.slice(0, -1);
        continue;
    }

    const nums =
        line.match(/\d+/g).map(Number);

    const attack =
        line.match(/(\w+) damage/)[1];

    const weak = new Set();
    const immune = new Set();

    const m =
        line.match(/\((.*?)\)/);

    if (m) {

        for (const part of m[1].split(';')) {

            const p = part.trim();

            if (p.startsWith('weak to')) {
                p.slice(8)
                    .split(',')
                    .forEach(x =>
                        weak.add(x.trim())
                    );
            }

            else if (
                p.startsWith('immune to')
            ) {
                p.slice(10)
                    .split(',')
                    .forEach(x =>
                        immune.add(x.trim())
                    );
            }
        }
    }

    groups.push({
        id: groups.length,
        army,
        units: nums[0],
        hp: nums[1],
        damage: nums[nums.length - 2],
        initiative: nums[nums.length - 1],
        type: attack,
        weak,
        immune
    });
}

function simulate(boost = 0) {

    const g = structuredClone(groups);

    for (const x of g) {
        x.weak = new Set(x.weak);
        x.immune = new Set(x.immune);

        if (
            x.army === 'Immune System'
        )
            x.damage += boost;
    }

    while (true) {

        const alive =
            g.filter(x => x.units > 0);

        const armies =
            new Set(
                alive.map(x => x.army)
            );

        if (armies.size === 1) {
            return [
                alive[0].army,
                alive.reduce(
                    (s, x) =>
                        s + x.units,
                    0
                )
            ];
        }

        const targets = new Map();
        const chosen = new Set();

        const order =
            [...alive].sort(
                (a, b) =>
                    (b.units * b.damage) -
                    (a.units * a.damage) ||
                    b.initiative -
                    a.initiative
            );

        for (const a of order) {

            let best = null;

            for (const b of alive) {

                if (
                    a.army === b.army ||
                    chosen.has(b.id)
                )
                    continue;

                let damage =
                    a.units *
                    a.damage;

                if (
                    b.immune.has(a.type)
                )
                    damage = 0;

                else if (
                    b.weak.has(a.type)
                )
                    damage *= 2;

                if (!damage)
                    continue;

                const score = [
                    damage,
                    b.units * b.damage,
                    b.initiative
                ];

                if (
                    !best ||
                    score[0] > best[0][0] ||
                    (
                        score[0] === best[0][0] &&
                        (
                            score[1] > best[0][1] ||
                            (
                                score[1] === best[0][1] &&
                                score[2] > best[0][2]
                            )
                        )
                    )
                ) {
                    best = [score, b];
                }
            }

            if (best) {
                targets.set(
                    a.id,
                    best[1]
                );

                chosen.add(
                    best[1].id
                );
            }
        }

        const attackOrder =
            [...alive].sort(
                (a, b) =>
                    b.initiative -
                    a.initiative
            );

        let killed = 0;

        for (const a of attackOrder) {

            if (
                a.units <= 0 ||
                !targets.has(a.id)
            )
                continue;

            const b =
                targets.get(a.id);

            if (b.units <= 0)
                continue;

            let damage =
                a.units *
                a.damage;

            if (
                b.immune.has(a.type)
            )
                damage = 0;

            else if (
                b.weak.has(a.type)
            )
                damage *= 2;

            const dead = Math.min(
                b.units,
                Math.floor(
                    damage / b.hp
                )
            );

            b.units -= dead;
            killed += dead;
        }

        if (killed === 0)
            return [null, 0];
    }
}

const p1 = simulate()[1];

console.log("Part 1:", p1);

let boost = 1;

while (true) {

    const [winner, units] =
        simulate(boost);

    if (
        winner ===
        "Immune System"
    ) {
        console.log(
            "Part 2:",
            units
        );
        break;
    }

    boost++;
}
```

# This Concludes Day 24 of The Advent of Code.
