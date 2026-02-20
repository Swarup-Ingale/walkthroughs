# URL
https://adventofcode.com/2016/day/2#part2

# Description
You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:
```
    1
  2 3 4
5 6 7 8 9
  A B C
    D
```
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:
```
You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.
```
Using the same instructions in your puzzle input, what is the correct bathroom code?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    # Diamond keypad (invalid positions are None)
    keypad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None]
    ]
    
    # Start at "5"
    row, col = 2, 0
    code = ""
    
    with open("input_02", "r") as file:
        lines = file.read().splitlines()
    
    for line in lines:
        for move in line:
            new_row, new_col = row, col
    
            if move == "U":
                new_row -= 1
            elif move == "D":
                new_row += 1
            elif move == "L":
                new_col -= 1
            elif move == "R":
                new_col += 1
    
            # Only move if the position is valid
            if (
                0 <= new_row < 5
                and 0 <= new_col < 5
                and keypad[new_row][new_col] is not None
            ):
                row, col = new_row, new_col
    
        # Record button after each line
        code += keypad[row][col]
    
    print("Bathroom code:", code)
  ```

# This Concludes the Day 02 of The Advent Of Code.
