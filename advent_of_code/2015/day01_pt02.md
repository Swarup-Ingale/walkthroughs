# URL
https://adventofcode.com/2015/day/1#part2

# Description
--- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:
```
) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
```
What is the position of the character that causes Santa to first enter the basement?

# Concept
Learn to enumerate the list of strings and find out at which position a certain event occurs

# Method of Solve
This is the code for solving part 02 of the the challenge :
```
  file_path = 'input_01_01' 
  
  with open(file_path, 'r') as file:
      raw_input = file.readlines()
  
  raw_string = raw_input[0]
  raw_list = list(raw_string)
  raw_list.pop() 
  
  enum_list = enumerate(raw_list, 1)
  
  def get_position_for_basement(enum_list):
    position = 0
    in_basement = False
    for i,j in enum_list:
      if j == '(':
        position += 1
      else:
        position -= 1
      if position == (-1):
        in_basement = True
      if in_basement:
        print(f"Santa enters the basement at position {i}.")
        break
  
  get_position_for_basement(enum_list)
```

# This Solves Day 01 of advent of code
