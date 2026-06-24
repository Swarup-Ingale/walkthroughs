# URL
https://adventofcode.com/2018/day/23#part2

# Description
Now, you just need to figure out where to position yourself so that you're actually teleported when the nanobots activate.

To increase the probability of success, you need to find the coordinate which puts you in range of the largest number of nanobots. If there are multiple, choose one closest to your position (0,0,0, measured by manhattan distance).

For example, given the following nanobot formation:
```
pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5
```
Many coordinates are in range of some of the nanobots in this formation. However, only the coordinate 12,12,12 is in range of the most nanobots: it is in range of the first five, but is not in range of the nanobot at 10,10,10. (All other coordinates are in range of fewer than five nanobots.) This coordinate's distance from 0,0,0 is 36.

Find the coordinates that are in range of the largest number of nanobots. What is the shortest manhattan distance between any of those points and 0,0,0?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re
import heapq

bots = []

for line in open("input_23"):
    bots.append(
        tuple(
            map(
                int,
                re.findall(r"-?\d+", line)
            )
        )
    )

xmin = min(x-r for x,y,z,r in bots)
xmax = max(x+r for x,y,z,r in bots)

size = 1

while size < xmax - xmin:
    size *= 2

pq = []

heapq.heappush(
    pq,
    (
        0,
        0,
        size,
        xmin,
        xmin,
        xmin
    )
)

while pq:

    negcount, dist, size, x, y, z = heapq.heappop(pq)

    if size == 1:
        print(dist)
        break

    half = size // 2

    for dx in [0, half]:
        for dy in [0, half]:
            for dz in [0, half]:

                nx = x + dx
                ny = y + dy
                nz = z + dz

                count = 0

                for bx, by, bz, br in bots:

                    d = (
                        max(0, abs(bx-nx)-half+1) +
                        max(0, abs(by-ny)-half+1) +
                        max(0, abs(bz-nz)-half+1)
                    )

                    if d <= br:
                        count += 1

                heapq.heappush(
                    pq,
                    (
                        -count,
                        abs(nx)+abs(ny)+abs(nz),
                        half,
                        nx,
                        ny,
                        nz
                    )
                )
```
- The Javascript version is as follows:
```
const fs = require('fs');

const bots = fs.readFileSync('input_23','utf8')
    .trim()
    .split('\n')
    .map(line =>
        line.match(/-?\d+/g)
            .map(Number)
    );

let minX = Infinity;
let maxX = -Infinity;

for (const [x,y,z,r] of bots) {
    minX = Math.min(minX, x-r);
    maxX = Math.max(maxX, x+r);
}

let size = 1;

while (size < maxX - minX)
    size *= 2;

const pq = [
    [0,0,size,minX,minX,minX]
];

while (pq.length) {

    pq.sort((a,b) =>
        a[0]-b[0] ||
        a[1]-b[1] ||
        a[2]-b[2]
    );

    const [
        neg,
        dist,
        s,
        x,
        y,
        z
    ] = pq.shift();

    if (s === 1) {
        console.log(dist);
        break;
    }

    const half = s / 2;

    for (const dx of [0,half])
    for (const dy of [0,half])
    for (const dz of [0,half]) {

        const nx = x + dx;
        const ny = y + dy;
        const nz = z + dz;

        let count = 0;

        for (const [bx,by,bz,br] of bots) {

            const d =
                Math.max(
                    0,
                    Math.abs(bx-nx)-half+1
                ) +
                Math.max(
                    0,
                    Math.abs(by-ny)-half+1
                ) +
                Math.max(
                    0,
                    Math.abs(bz-nz)-half+1
                );

            if (d <= br)
                count++;
        }

        pq.push([
            -count,
            Math.abs(nx)+Math.abs(ny)+Math.abs(nz),
            half,
            nx,
            ny,
            nz
        ]);
    }
}
```

# This Concludes Day 23 of The Advent of Code.
