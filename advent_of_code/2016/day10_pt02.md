# URL
https://adventofcode.com/2016/day/10#part2

# Description
What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    from collections import defaultdict, deque
    
    bots = defaultdict(list)
    rules = {}
    outputs = {}
    
    with open("input_10", "r") as f:
        lines = f.read().strip().splitlines()
    
    # Parse instructions
    for line in lines:
        parts = line.split()
        if line.startswith("value"):
            value = int(parts[1])
            bot = int(parts[-1])
            bots[bot].append(value)
        else:
            bot = int(parts[1])
            low_type, low_id = parts[5], int(parts[6])
            high_type, high_id = parts[10], int(parts[11])
            rules[bot] = (low_type, low_id, high_type, high_id)
    
    # Queue bots that are ready
    queue = deque([b for b in bots if len(bots[b]) == 2])
    
    # Process
    while queue:
        bot = queue.popleft()
        low, high = sorted(bots[bot])
    
        low_type, low_id, high_type, high_id = rules[bot]
    
        # Give low chip
        if low_type == "bot":
            bots[low_id].append(low)
            if len(bots[low_id]) == 2:
                queue.append(low_id)
        else:
            outputs[low_id] = low
    
        # Give high chip
        if high_type == "bot":
            bots[high_id].append(high)
            if len(bots[high_id]) == 2:
                queue.append(high_id)
        else:
            outputs[high_id] = high
    
        bots[bot] = []
    
    result = outputs[0] * outputs[1] * outputs[2]
    print("Product of outputs 0, 1, and 2:", result)
  ```

# This Concludes the Day 10 of The Advent of Code.
