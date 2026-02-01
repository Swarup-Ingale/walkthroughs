# URL
https://adventofcode.com/2015/day/1

# Description
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:
```
(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?
```
# Concept
Counting Characters and returning an result based on the counting

# Method of Solve
This Python code will solve first part of the challenge :
```
  file_path = 'input.txt' # path to input your input file

  with open(file_path, 'r') as file:
      raw_input = file.readlines()
  
  raw_string = raw_input[0]
  raw_list = list(raw_string)
  raw_list.pop() 
  
  def get_floor(list):
    up_floor = 0
    down_floor = 0
    for i in list:
      if i == '(':
        up_floor += 1
      else:
        down_floor += 1
    final_floor = up_floor - down_floor
    return final_floor
  
  answer = get_floor(raw_list)
  
  print(f"The answer is {answer}")
```

# This one solves the first part of the code 
