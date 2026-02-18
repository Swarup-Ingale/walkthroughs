# URL
https://adventofcode.com/2015/day/21

# Description
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:
```
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
```
You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:
```
The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
```
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

# Method of Solve
- The part 01 of this challenge can be solved using the following code :
  ```
    import itertools
    import math
    
    
    with open("input_21_01") as f:
        lines = f.readlines()
    
    boss_hp = int(lines[0].split(":")[1].strip())
    boss_damage = int(lines[1].split(":")[1].strip())
    boss_armor = int(lines[2].split(":")[1].strip())
    # SHOP
    
    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    ]
    
    armor = [
        (0, 0, 0),      # No armor
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    ]
    
    rings = [
        (0, 0, 0),      # Dummy ring (no ring)
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]
    
    PLAYER_HP = 100
    min_cost = float("inf")
    
    # SIMULATION 
    
    for weapon in weapons:
        for arm in armor:
            for ring1, ring2 in itertools.combinations(rings, 2):
    
                cost = weapon[0] + arm[0] + ring1[0] + ring2[0]
                damage = weapon[1] + arm[1] + ring1[1] + ring2[1]
                defense = weapon[2] + arm[2] + ring1[2] + ring2[2]
    
                player_attack = max(1, damage - boss_armor)
                boss_attack = max(1, boss_damage - defense)
    
                player_turns = math.ceil(boss_hp / player_attack)
                boss_turns = math.ceil(PLAYER_HP / boss_attack)
    
                if player_turns <= boss_turns:
                    min_cost = min(min_cost, cost)
    
    print("Least amount of gold to win:", min_cost)
  ```
- This Solves the part 01 of this challenge.
