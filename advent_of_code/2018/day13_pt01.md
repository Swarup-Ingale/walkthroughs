# URL
https://adventofcode.com/2018/day/13

# Description
A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are very busy pushing things around in carts on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for another 1000 years, the Elves seem to be making this up as they go along. They haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and intersections (+). Curves connect exactly two perpendicular pieces of track; for example, this is a closed loop:
```
/----\
|    |
|    |
\----/
```
Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning right, or continuing straight. Here are two loops connected by two intersections:
```
/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/
```
Several carts are also on the tracks. Carts always face either up (^), down (v), left (<), or right (>). (On your initial map, the track under each cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it turns left the first time, goes straight the second time, turns right the third time, and then repeats those directions starting again with left the fourth time, straight the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is, the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their current location: carts on the top row move first (acting from left to right), then carts on the second row move (again from left to right), then carts on the third row, and so on. Once each cart has moved one step, the process repeats; each of these loops is called a tick.

For example, suppose there are two carts on a straight track:
```
|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |
```
First, the top cart moves. It is facing down (v), so it moves down one square. Second, the bottom cart moves. It is facing up (^), so it moves up one square. Because all carts have moved, the first tick ends. Then, the process repeats, starting with the first cart. The first cart moves down, then the second cart moves up - right into the first cart, colliding with it! (The location of the crash is marked with an X.) This ends the second and last tick.

Here is a longer example:
```
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   

/-->\        
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/   

/---v        
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/   

/---\        
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/   

/---\        
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/   

/---\        
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/   

/---\        
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/   

/---\        
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/   

/---\        
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/   

/---\        
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/   
```
After following their respective paths for a while, the carts eventually crash. To help prevent crashes, you'd like to know the location of the first crash. Locations are given in X,Y coordinates, where the furthest left column is X=0 and the furthest top row is Y=0:
```
           111
 0123456789012
0/---\        
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/   
```
In this example, the location of the first crash is 7,3.

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python version is as follows:
```
grid = []
carts = []

with open("input_13") as f:

    for y, line in enumerate(f):

        row = list(line.rstrip("\n"))

        for x, c in enumerate(row):

            if c in "^v<>":

                carts.append(
                    [x, y, c, 0]
                )

                row[x] = (
                    "|"
                    if c in "^v"
                    else "-"
                )

        grid.append(row)

dirs = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

left = {
    "^": "<",
    "<": "v",
    "v": ">",
    ">": "^",
}

right = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

while True:

    carts.sort(
        key=lambda c: (c[1], c[0])
    )

    positions = {
        (c[0], c[1])
        for c in carts
    }

    for cart in carts:

        positions.remove(
            (cart[0], cart[1])
        )

        dx, dy = dirs[cart[2]]

        cart[0] += dx
        cart[1] += dy

        pos = (
            cart[0],
            cart[1]
        )

        if pos in positions:

            print(
                f"{pos[0]},{pos[1]}"
            )
            raise SystemExit

        positions.add(pos)

        track = grid[
            cart[1]
        ][
            cart[0]
        ]

        if track == "/":

            cart[2] = {
                "^": ">",
                ">": "^",
                "v": "<",
                "<": "v"
            }[cart[2]]

        elif track == "\\":

            cart[2] = {
                "^": "<",
                "<": "^",
                "v": ">",
                ">": "v"
            }[cart[2]]

        elif track == "+":

            if cart[3] == 0:
                cart[2] = left[cart[2]]

            elif cart[3] == 2:
                cart[2] = right[cart[2]]

            cart[3] = (
                cart[3] + 1
            ) % 3
```
- The Javascript version is as follows :
```
const fs = require('fs');

const lines = fs
    .readFileSync(
        'input_13',
        'utf8'
    )
    .split('\n');

const grid = [];
const carts = [];

for (
    let y = 0;
    y < lines.length;
    y++
) {

    const row =
        lines[y].split('');

    for (
        let x = 0;
        x < row.length;
        x++
    ) {

        const c = row[x];

        if ('^v<>'.includes(c)) {

            carts.push({
                x,
                y,
                dir: c,
                turn: 0
            });

            row[x] =
                '^v'.includes(c)
                    ? '|'
                    : '-';
        }
    }

    grid.push(row);
}

const dirs = {
    '^':[0,-1],
    'v':[0,1],
    '<':[-1,0],
    '>':[1,0]
};

const left = {
    '^':'<',
    '<':'v',
    'v':'>',
    '>':'^'
};

const right = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^'
};

while (true) {

    carts.sort(
        (a,b)=>
            a.y-b.y ||
            a.x-b.x
    );

    const pos =
        new Set(
            carts.map(
                c =>
                    `${c.x},${c.y}`
            )
        );

    for (const cart of carts) {

        pos.delete(
            `${cart.x},${cart.y}`
        );

        const [dx,dy] =
            dirs[cart.dir];

        cart.x += dx;
        cart.y += dy;

        const key =
            `${cart.x},${cart.y}`;

        if (pos.has(key)) {

            console.log(key);
            process.exit();
        }

        pos.add(key);

        const track =
            grid[cart.y][cart.x];

        if (track === '/') {

            cart.dir = {
                '^':'>',
                '>':'^',
                'v':'<',
                '<':'v'
            }[cart.dir];

        } else if (
            track === '\\'
        ) {

            cart.dir = {
                '^':'<',
                '<':'^',
                'v':'>',
                '>':'v'
            }[cart.dir];

        } else if (
            track === '+'
        ) {

            if (
                cart.turn === 0
            )
                cart.dir =
                    left[cart.dir];

            else if (
                cart.turn === 2
            )
                cart.dir =
                    right[cart.dir];

            cart.turn =
                (cart.turn+1)%3;
        }
    }
}
```
- This Solves the Part 01 of this challenge.
