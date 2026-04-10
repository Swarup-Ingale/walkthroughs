# URL
https://adventofcode.com/2017/day/20#part2

# Description
To simplify the problem further, the GPU would like to remove any particles that collide. Particles collide if their positions ever exactly match. Because particles are updated simultaneously, more than two particles can collide at the same time and place. Once particles collide, they are removed and cannot collide with anything else after that tick.

For example:
```
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
```
```
p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)   
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>
```
```
p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)      
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>
```
```
------destroyed by collision------    
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)         
```
```
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>
```
In this example, particles 0, 1, and 2 are simultaneously destroyed at the time and place marked X. On the next tick, particle 3 passes through unharmed.

How many particles are left after all collisions are resolved?

# Method Of Solve
- The Part 02 of this challenge can be solved using the following code:
```
from collections import defaultdict


def parse(line):
    parts = line.strip().split(", ")
    p = list(map(int, parts[0][3:-1].split(',')))
    v = list(map(int, parts[1][3:-1].split(',')))
    a = list(map(int, parts[2][3:-1].split(',')))
    return p, v, a


if __name__ == "__main__":
    particles = []

    with open("input_20") as f:
        for line in f:
            p, v, a = parse(line)
            particles.append([p, v, a])

    for _ in range(1000):  # simulate enough time
        positions = defaultdict(list)

        # update particles
        for i, (p, v, a) in enumerate(particles):
            v[0] += a[0]
            v[1] += a[1]
            v[2] += a[2]

            p[0] += v[0]
            p[1] += v[1]
            p[2] += v[2]

            positions[tuple(p)].append(i)

        # remove collisions
        new_particles = []
        for pos, idxs in positions.items():
            if len(idxs) == 1:
                new_particles.append(particles[idxs[0]])

        particles = new_particles

    print("Remaining particles:", len(particles))
```

# This Concludes Day 20 of The Advent of Code.
