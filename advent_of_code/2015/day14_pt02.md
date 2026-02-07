# URL
https://adventofcode.com/2015/day/14#part2

# Description
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

# Method of Solve
- The Part 02 of the challenge can be solved using the following code:
  ```
    import re

    TIME = 2503
    
    reindeer = {}
    
    with open("input_14_01") as f:
        for line in f:
            m = re.match(
                r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
                line.strip()
            )
            name, speed, fly, rest = m.groups()
            reindeer[name] = {
                "speed": int(speed),
                "fly": int(fly),
                "rest": int(rest),
                "distance": 0,
                "points": 0,
                "state": "fly",
                "time_left": int(fly),
            }
    
    # Simulate second by second
    for _ in range(TIME):
        for r in reindeer.values():
            if r["state"] == "fly":
                r["distance"] += r["speed"]
    
            r["time_left"] -= 1
            if r["time_left"] == 0:
                if r["state"] == "fly":
                    r["state"] = "rest"
                    r["time_left"] = r["rest"]
                else:
                    r["state"] = "fly"
                    r["time_left"] = r["fly"]
    
        # Award points
        max_dist = max(r["distance"] for r in reindeer.values())
        for r in reindeer.values():
            if r["distance"] == max_dist:
                r["points"] += 1
    
    # Result
    print(max(r["points"] for r in reindeer.values()))
  ```

# This Concludes the Day 14 of the Advent of Code
