# URL
https://adventofcode.com/2018/day/24

# Description
After a weird buzzing noise, you appear back at the man's cottage. He seems relieved to see his friend, but quickly notices that the little reindeer caught some kind of cold while out exploring.

The portly man explains that this reindeer's immune system isn't similar to regular reindeer immune systems:

The immune system and the infection each have an army made up of several groups; each group consists of one or more identical units. The armies repeatedly fight until only one army has units remaining.

Units within a group all have the same hit points (amount of damage a unit can take before it is destroyed), attack damage (the amount of damage each unit deals), an attack type, an initiative (higher initiative units attack first and win ties), and sometimes weaknesses or immunities. Here is an example group:

18 units each with 729 hit points (weak to fire; immune to cold, slashing)
 with an attack that does 8 radiation damage at initiative 10

Each group also has an effective power: the number of units in that group multiplied by their attack damage. The above group has an effective power of 18 * 8 = 144. Groups never have zero or negative units; instead, the group is removed from combat.

Each fight consists of two phases: target selection and attacking.

During the target selection phase, each group attempts to choose one target. In decreasing order of effective power, groups choose their targets; in a tie, the group with the higher initiative chooses first. The attacking group chooses to target the group in the enemy army to which it would deal the most damage (after accounting for weaknesses and immunities, but not accounting for whether the defending group has enough units to actually receive all of that damage).

If an attacking group is considering two defending groups to which it would deal equal damage, it chooses to target the defending group with the largest effective power; if there is still a tie, it chooses the defending group with the highest initiative. If it cannot deal any defending groups damage, it does not choose a target. Defending groups can only be chosen as a target by one attacking group.

At the end of the target selection phase, each group has selected zero or one groups to attack, and each group is being attacked by zero or one groups.

During the attacking phase, each group deals damage to the target it selected, if any. Groups attack in decreasing order of initiative, regardless of whether they are part of the infection or the immune system. (If a group contains no units, it cannot attack.)

The damage an attacking group deals to a defending group depends on the attacking group's attack type and the defending group's immunities and weaknesses. By default, an attacking group would deal damage equal to its effective power to the defending group. However, if the defending group is immune to the attacking group's attack type, the defending group instead takes no damage; if the defending group is weak to the attacking group's attack type, the defending group instead takes double damage.

The defending group only loses whole units from damage; damage is always dealt in such a way that it kills the most units possible, and any remaining damage to a unit that does not immediately kill it is ignored. For example, if a defending group contains 10 units with 10 hit points each and receives 75 damage, it loses exactly 7 units and is left with 3 units at full health.

After the fight is over, if both armies still contain units, a new fight begins; combat only ends once one army has lost all of its units.

For example, consider the following armies:
```
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with
 an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
 slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack
 that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire,
 cold) with an attack that does 12 slashing damage at initiative 4
```
If these armies were to enter combat, the following fights, including details during the target selection and attacking phases, would take place:
```
Immune System:
Group 1 contains 17 units
Group 2 contains 989 units
Infection:
Group 1 contains 801 units
Group 2 contains 4485 units

Infection group 1 would deal defending group 1 185832 damage
Infection group 1 would deal defending group 2 185832 damage
Infection group 2 would deal defending group 2 107640 damage
Immune System group 1 would deal defending group 1 76619 damage
Immune System group 1 would deal defending group 2 153238 damage
Immune System group 2 would deal defending group 1 24725 damage

Infection group 2 attacks defending group 2, killing 84 units
Immune System group 2 attacks defending group 1, killing 4 units
Immune System group 1 attacks defending group 2, killing 51 units
Infection group 1 attacks defending group 1, killing 17 units

Immune System:
Group 2 contains 905 units
Infection:
Group 1 contains 797 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 184904 damage
Immune System group 2 would deal defending group 1 22625 damage
Immune System group 2 would deal defending group 2 22625 damage

Immune System group 2 attacks defending group 1, killing 4 units
Infection group 1 attacks defending group 2, killing 144 units

Immune System:
Group 2 contains 761 units
Infection:
Group 1 contains 793 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 183976 damage
Immune System group 2 would deal defending group 1 19025 damage
Immune System group 2 would deal defending group 2 19025 damage

Immune System group 2 attacks defending group 1, killing 4 units
Infection group 1 attacks defending group 2, killing 143 units

Immune System:
Group 2 contains 618 units
Infection:
Group 1 contains 789 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 183048 damage
Immune System group 2 would deal defending group 1 15450 damage
Immune System group 2 would deal defending group 2 15450 damage

Immune System group 2 attacks defending group 1, killing 3 units
Infection group 1 attacks defending group 2, killing 143 units

Immune System:
Group 2 contains 475 units
Infection:
Group 1 contains 786 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 182352 damage
Immune System group 2 would deal defending group 1 11875 damage
Immune System group 2 would deal defending group 2 11875 damage

Immune System group 2 attacks defending group 1, killing 2 units
Infection group 1 attacks defending group 2, killing 142 units

Immune System:
Group 2 contains 333 units
Infection:
Group 1 contains 784 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181888 damage
Immune System group 2 would deal defending group 1 8325 damage
Immune System group 2 would deal defending group 2 8325 damage

Immune System group 2 attacks defending group 1, killing 1 unit
Infection group 1 attacks defending group 2, killing 142 units

Immune System:
Group 2 contains 191 units
Infection:
Group 1 contains 783 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181656 damage
Immune System group 2 would deal defending group 1 4775 damage
Immune System group 2 would deal defending group 2 4775 damage

Immune System group 2 attacks defending group 1, killing 1 unit
Infection group 1 attacks defending group 2, killing 142 units

Immune System:
Group 2 contains 49 units
Infection:
Group 1 contains 782 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181424 damage
Immune System group 2 would deal defending group 1 1225 damage
Immune System group 2 would deal defending group 2 1225 damage

Immune System group 2 attacks defending group 1, killing 0 units
Infection group 1 attacks defending group 2, killing 49 units

Immune System:
No groups remain.
Infection:
Group 1 contains 782 units
Group 2 contains 4434 units
```
In the example above, the winning army ends up with 782 + 4434 = 5216 units.

You scan the reindeer's condition (your puzzle input); the white-bearded man looks nervous. As it stands now, how many units would the winning army have?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
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
- This Solves Part 01 of this challenge.
