# URL
https://adventofcode.com/2019/day/6

# Description
You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:
```
                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
```
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.

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
```
Visually, the above map of orbits looks like this:
```
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
```
In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:
```
    D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
    L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
    COM orbits nothing.
```
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
with open("input06", "r") as f:
	parent = {}

	for line in f:
		a, b = line.strip().split(")")
		parent[b] = a

cache = {}

def depth(node):
	if node == "COM":
		return 0

	if node in cache:
		return cache[node]

	cache[node] = 1 + depth(parent[node])
	return cache[node]

answer = sum(depth(node) for node in parent)
print (answer)
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

const cache = {};

function depth(node) {
	if (node === "COM") {
		return 0;
	}

	if (cache[node] !== undefined) {
		return cache[node];
	}

	cache[node] = 1 + depth(parent[node]);

	return cache[node];
}

let answer = 0;

for (const node in parent) {
	answer += depth(node);
}

console.log(answer);
```
- This Solves The Part 01 of this challenge.
