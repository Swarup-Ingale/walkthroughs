# URL
https://adventofcode.com/2017/day/7#part2

# Description
The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:
```
ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
```
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import defaultdict, Counter
    
    weights = {}
    children = defaultdict(list)
    all_nodes = set()
    child_nodes = set()
    
    # Read input
    with open("input_07", "r") as f:
        for line in f:
            parts = line.strip().split("->")
            
            left = parts[0].split()
            name = left[0]
            weight = int(left[1].strip("()"))
    
            weights[name] = weight
            all_nodes.add(name)
    
            if len(parts) > 1:
                childs = parts[1].strip().split(", ")
                children[name] = childs
                child_nodes.update(childs)
    
    # Find root
    root = (all_nodes - child_nodes).pop()
    
    def total_weight(node):
        sub_weights = [total_weight(c) for c in children[node]]
    
        if len(set(sub_weights)) > 1:
            count = Counter(sub_weights)
    
            correct = count.most_common(1)[0][0]
            wrong = [w for w in sub_weights if w != correct][0]
    
            wrong_child = children[node][sub_weights.index(wrong)]
    
            diff = correct - wrong
            corrected_weight = weights[wrong_child] + diff
    
            print("Correct weight:", corrected_weight)
            exit()
    
        return weights[node] + sum(sub_weights)
    
    total_weight(root)
  ```

# This Concludes Day 07 of The Advent of Code.
