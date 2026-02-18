# URL
https://adventofcode.com/2015/day/21#part2

# Description
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
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
    max_cost = 0
    
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
    
                if player_turns > boss_turns:
                    max_cost = max(max_cost, cost)
    
    print("Least amount of gold to win:", max_cost)
  ```

# This Concludes the part 02 of The Advent of Code.
