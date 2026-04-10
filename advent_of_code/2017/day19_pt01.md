# URL
https://adventofcode.com/2017/day/19

# Description
Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:
```
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
```
Given this diagram, the packet needs to take the following path:

- Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
- Travel right, up, and right, passing through B in the process.
- Continue down (collecting C), right, and up (collecting D).
- Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)

# Method Of Solve
- The Part 01 of this challenge can be solved using the following code:
```
def part1(grid):
    rows = len(grid)
    cols = len(grid[0])

    # find start (first | in top row)
    x = 0
    y = grid[0].index('|')

    dx, dy = 1, 0  # moving DOWN
    letters = []

    while True:
        x += dx
        y += dy

        if x < 0 or y < 0 or x >= rows or y >= cols:
            break

        char = grid[x][y]

        if char == ' ':
            break

        if char.isalpha():
            letters.append(char)

        elif char == '+':
            # turn: try perpendicular directions
            for ndx, ndy in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (ndx, ndy) != (-dx, -dy):  # don't go back
                    nx, ny = x + ndx, y + ndy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] != ' ':
                            dx, dy = ndx, ndy
                            break

    return ''.join(letters)


if __name__ == "__main__":
    with open("input_19") as f:
        grid = [list(line.rstrip('\n')) for line in f]

    print("Letters:", part1(grid))
```
- This Solves the Part 01 of this challenge.
