# URL
https://adventofcode.com/2018/day/10

# Description
It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle, and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly enough that it takes hours to align them, but have so much momentum that they only stay aligned for a second. If you blink at the wrong time, it might be hours before another message appears.

You can see these points of light floating in the distance, and record their position in the sky and their velocity, the relative change in position per second (your puzzle input). The coordinates are all given from your perspective; given enough time, those positions and velocities will move the points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.

For example, suppose you note the following points:
```
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
```
Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative) or right (positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position. So, a point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this point's initial position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:
```
Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................
```
After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will take many more seconds to appear.

What message will eventually appear in the sky?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
import re

points = []

with open("input_10") as f:
    for line in f:
        x, y, vx, vy = map(
            int,
            re.findall(r"-?\d+", line)
        )

        points.append([x, y, vx, vy])


def area(points):

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    return (
        max(xs) - min(xs)
    ) * (
        max(ys) - min(ys)
    )


best_points = None
best_area = float("inf")

for t in range(20000):

    current_area = area(points)

    if current_area < best_area:
        best_area = current_area
        best_points = [
            p[:] for p in points
        ]

    for p in points:
        p[0] += p[2]
        p[1] += p[3]


xs = [p[0] for p in best_points]
ys = [p[1] for p in best_points]

min_x = min(xs)
max_x = max(xs)

min_y = min(ys)
max_y = max(ys)

grid = {
    (p[0], p[1])
    for p in best_points
}

for y in range(min_y, max_y + 1):

    row = ""

    for x in range(
        min_x,
        max_x + 1
    ):
        row += (
            "#"
            if (x, y) in grid
            else "."
        )

    print(row)
```
- The Javascript version is :
```
const fs = require('fs');

const points = fs
    .readFileSync('input_10', 'utf8')
    .trim()
    .split('\n')
    .map(line =>
        line.match(/-?\d+/g)
            .map(Number)
    );

function area(points) {

    const xs =
        points.map(p => p[0]);

    const ys =
        points.map(p => p[1]);

    return (
        Math.max(...xs) -
        Math.min(...xs)
    ) *
    (
        Math.max(...ys) -
        Math.min(...ys)
    );
}

let bestArea =
    Number.MAX_SAFE_INTEGER;

let bestPoints = null;

for (
    let t = 0;
    t < 20000;
    t++
) {

    const current =
        area(points);

    if (
        current < bestArea
    ) {

        bestArea = current;

        bestPoints =
            points.map(
                p => [...p]
            );
    }

    for (const p of points) {

        p[0] += p[2];
        p[1] += p[3];
    }
}

const xs =
    bestPoints.map(p => p[0]);

const ys =
    bestPoints.map(p => p[1]);

const minX =
    Math.min(...xs);

const maxX =
    Math.max(...xs);

const minY =
    Math.min(...ys);

const maxY =
    Math.max(...ys);

const set =
    new Set(
        bestPoints.map(
            p => `${p[0]},${p[1]}`
        )
    );

for (
    let y = minY;
    y <= maxY;
    y++
) {

    let row = '';

    for (
        let x = minX;
        x <= maxX;
        x++
    ) {

        row +=
            set.has(
                `${x},${y}`
            )
                ? '#'
                : '.';
    }

    console.log(row);
}
```
- This Solves The Part 01 of this challenge.
