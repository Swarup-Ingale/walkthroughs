# URL
https://adventofcode.com/2019/day/6#part2

# Description
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:
```
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
```
Visually, the above map of orbits looks like this:
```
                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
```
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:
```
    K to J
    J to E
    E to D
    D to I
```
Afterward, the map of orbits looks like this:
```
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
```
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input06", "r") as f:
	parent = {}

	for line in f:
		a, b = line.strip().split(")")
		parent[b] = a

dist = {}

node = parent["YOU"]
steps = 0

while node != "COM":
	dist[node] = steps
	node = parent[node]
	steps += 1

dist["COM"] = steps

node = parent["SAN"]
steps = 0

while node not in dist:
	node = parent[node]
	steps += 1

print (steps + dist[node])
```
- The Javascript version is as follows:
```
const fs = require("fs");

const lines = fs
	.readFileSync("input06", "utf8")
	.trim()
	.split("\n");

const parent = {};

for (const line of lines) {
	const [a, b] = line.split(")");
	parent[b] = a;
}

const dist = {};

let node = parent["YOU"];
let steps = 0;

while (node !== "COM") {
	dist[node] = steps;
	node = parent[node];
	steps++;
}

dist["COM"] = steps;

node = parent["SAN"];
steps = 0;

while (!(node in dist)) {
	node = parent[node];
	steps++;
}

console.log(steps + dist[node]);
```

# This Concludes Day 06 of The Advent of Code.
