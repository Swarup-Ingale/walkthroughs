# URL
https://adventofcode.com/2018/day/22#part2

# Description
Okay, it's time to go rescue the man's friend.

As you leave, he hands you some tools: a torch and some climbing gear. You can't equip both tools at once, but you can choose to use neither.

Tools can only be used in certain regions:
```
    In rocky regions, you can use the climbing gear or the torch. You cannot use neither (you'll likely slip and fall).
    In wet regions, you can use the climbing gear or neither tool. You cannot use the torch (if it gets wet, you won't have a light source).
    In narrow regions, you can use the torch or neither tool. You cannot use the climbing gear (it's too bulky to fit).
```
You start at 0,0 (the mouth of the cave) with the torch equipped and must reach the target coordinates as quickly as possible. The regions with negative X or Y are solid rock and cannot be traversed. The fastest route might involve entering regions beyond the X or Y coordinate of the target.

You can move to an adjacent region (up, down, left, or right; never diagonally) if your currently equipped tool allows you to enter that region. Moving to an adjacent region takes one minute. (For example, if you have the torch equipped, you can move between rocky and narrow regions, but cannot enter wet regions.)

You can change your currently equipped tool or put both away if your new equipment would be valid for your current region. Switching to using the climbing gear, torch, or neither always takes seven minutes, regardless of which tools you start with. (For example, if you are in a rocky region, you can switch from the torch to the climbing gear, but you cannot switch to neither.)

Finally, once you reach the target, you need the torch equipped before you can find him in the dark. The target is always in a rocky region, so if you arrive there with climbing gear equipped, you will need to spend seven minutes switching to your torch.

For example, using the same cave system as above, starting in the top left corner (0,0) and moving to the bottom right corner (the target, 10,10) as quickly as possible, one possible route is as follows, with your current position marked X:
```
Initially:
X=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down:
M=.|=.|.|=.|=|=.
X|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.X=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using the torch to neither tool:
M=.|=.|.|=.|=|=.
.X=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right 3:
M=.|=.|.|=.|=|=.
.|=|X|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using neither tool to the climbing gear:
M=.|=.|.|=.|=|=.
.|=|X|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down 7:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..X==..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..=X=..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down 3:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||.X.|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||..X|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.X..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right 4:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=X||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Up 2:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===X===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using the climbing gear to the torch:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===X===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||
```
This is tied with other routes as the fastest way to reach the target: 45 minutes. In it, 21 minutes are spent switching tools (three times, seven minutes each) and the remaining 24 minutes are spent moving.

What is the fewest number of minutes you can take to reach the target?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re
import heapq

lines = open("input_22").read().splitlines()

depth = int(re.search(r"\d+", lines[0]).group())
tx, ty = map(int, re.findall(r"\d+", lines[1]))

erosion = {}

def er(x, y):

    if (x, y) in erosion:
        return erosion[(x, y)]

    if (x, y) in [(0,0), (tx,ty)]:
        g = 0
    elif y == 0:
        g = x * 16807
    elif x == 0:
        g = y * 48271
    else:
        g = er(x-1, y) * er(x, y-1)

    erosion[(x, y)] = (g + depth) % 20183

    return erosion[(x, y)]

allowed = {
    0: {0,1},
    1: {1,2},
    2: {0,2}
}

pq = [(0, 0, 0, 0)]

seen = {}

while pq:

    t, x, y, tool = heapq.heappop(pq)

    state = (x, y, tool)

    if state in seen:
        continue

    seen[state] = t

    if (x, y, tool) == (tx, ty, 0):
        print(t)
        break

    region = er(x, y) % 3

    for ntool in allowed[region]:
        if ntool != tool:
            heapq.heappush(
                pq,
                (t + 7, x, y, ntool)
            )

    for dx, dy in [
        (0,-1),
        (0,1),
        (-1,0),
        (1,0)
    ]:

        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0:
            continue

        nregion = er(nx, ny) % 3

        if tool in allowed[nregion]:
            heapq.heappush(
                pq,
                (t + 1, nx, ny, tool)
            )
```
- The Javascript version is as follows:
```
const fs = require('fs');

const lines =
    fs.readFileSync('input_22','utf8')
      .trim()
      .split('\n');

const depth =
    Number(lines[0].match(/\d+/)[0]);

const [tx, ty] =
    lines[1]
        .match(/\d+/g)
        .map(Number);

const erosion = {};

function er(x, y) {

    const k = `${x},${y}`;

    if (k in erosion)
        return erosion[k];

    let g;

    if (
        (x === 0 && y === 0) ||
        (x === tx && y === ty)
    )
        g = 0;

    else if (y === 0)
        g = x * 16807;

    else if (x === 0)
        g = y * 48271;

    else
        g =
            er(x-1,y) *
            er(x,y-1);

    erosion[k] =
        (g + depth) % 20183;

    return erosion[k];
}

const allowed = {
    0: [0,1],
    1: [1,2],
    2: [0,2]
};

const pq = [[0,0,0,0]];
const seen = new Set();

while (pq.length) {

    pq.sort((a,b)=>a[0]-b[0]);

    const [t,x,y,tool] =
        pq.shift();

    const key =
        `${x},${y},${tool}`;

    if (seen.has(key))
        continue;

    seen.add(key);

    if (
        x === tx &&
        y === ty &&
        tool === 0
    ) {
        console.log(t);
        break;
    }

    const region =
        er(x,y) % 3;

    for (
        const ntool of
        allowed[region]
    ) {
        if (ntool !== tool)
            pq.push([
                t+7,
                x,
                y,
                ntool
            ]);
    }

    for (const [dx,dy] of [
        [0,-1],[0,1],
        [-1,0],[1,0]
    ]) {

        const nx = x + dx;
        const ny = y + dy;

        if (
            nx < 0 ||
            ny < 0
        ) continue;

        const nr =
            er(nx,ny) % 3;

        if (
            allowed[nr]
                .includes(tool)
        ) {
            pq.push([
                t+1,
                nx,
                ny,
                tool
            ]);
        }
    }
}
```

# This Concludes Day 22 of The Advent of Code.
