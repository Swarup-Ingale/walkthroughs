# URL
https://adventofcode.com/2015/day/22#part2

# Description
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    import math
    from copy import deepcopy
    
    with open("input_22_01") as f:
        boss_hp = int(f.readline().split(":")[1])
        boss_damage = int(f.readline().split(":")[1])
    
    # SPELLS 
    
    SPELLS = {
        "Magic Missile": {"cost": 53},
        "Drain": {"cost": 73},
        "Shield": {"cost": 113, "timer": 6},
        "Poison": {"cost": 173, "timer": 6},
        "Recharge": {"cost": 229, "timer": 5},
    }
    
    BEST_MANA = math.inf
    
    # EFFECT HANDLER 
    
    def apply_effects(state):
        armor = 0
    
        if state["shield"] > 0:
            armor = 7
            state["shield"] -= 1
    
        if state["poison"] > 0:
            state["boss_hp"] -= 3
            state["poison"] -= 1
    
        if state["recharge"] > 0:
            state["mana"] += 101
            state["recharge"] -= 1
    
        return armor
    
    # DFS
    
    def dfs(state, hard_mode=False):
        global BEST_MANA
    
        # Hard mode penalty
        if hard_mode:
            state["player_hp"] -= 1
            if state["player_hp"] <= 0:
                return
    
        # Apply effects (player turn)
        armor = apply_effects(state)
        if state["boss_hp"] <= 0:
            BEST_MANA = min(BEST_MANA, state["mana_spent"])
            return
    
        for spell, info in SPELLS.items():
            if state["mana"] < info["cost"]:
                continue
    
            # Can't cast active effect
            if spell == "Shield" and state["shield"] > 0: continue
            if spell == "Poison" and state["poison"] > 0: continue
            if spell == "Recharge" and state["recharge"] > 0: continue
    
            next_state = deepcopy(state)
            next_state["mana"] -= info["cost"]
            next_state["mana_spent"] += info["cost"]
    
            if next_state["mana_spent"] >= BEST_MANA:
                continue
    
            # Cast spell
            if spell == "Magic Missile":
                next_state["boss_hp"] -= 4
            elif spell == "Drain":
                next_state["boss_hp"] -= 2
                next_state["player_hp"] += 2
            elif spell == "Shield":
                next_state["shield"] = 6
            elif spell == "Poison":
                next_state["poison"] = 6
            elif spell == "Recharge":
                next_state["recharge"] = 5
    
            # Boss dead?
            if next_state["boss_hp"] <= 0:
                BEST_MANA = min(BEST_MANA, next_state["mana_spent"])
                continue
    
            # Apply effects (boss turn)
            armor = apply_effects(next_state)
            if next_state["boss_hp"] <= 0:
                BEST_MANA = min(BEST_MANA, next_state["mana_spent"])
                continue
    
            # Boss attacks
            damage = max(1, boss_damage - armor)
            next_state["player_hp"] -= damage
            if next_state["player_hp"] <= 0:
                continue
    
            dfs(next_state, hard_mode)
    
    # INITIAL STATE
    
    initial_state = {
        "player_hp": 50,
        "mana": 500,
        "boss_hp": boss_hp,
        "shield": 0,
        "poison": 0,
        "recharge": 0,
        "mana_spent": 0,
    }
    
    # PART 2
    
    BEST_MANA = math.inf
    dfs(deepcopy(initial_state), hard_mode=True)
    print("Hard mode Mana Requirements:", BEST_MANA)
  ```

# This Concludes the Day 22 of The Advent of Code.
