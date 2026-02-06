# URL
https://adventofcode.com/2015/day/12

# Description
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:
```
[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
```
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

# Method of Solve
- The part 01 of this challenge can be solved using the following code :
  ```
    import json

    def sum_numbers(data):
        if isinstance(data, int):
            return data
        elif isinstance(data, list):
            return sum(sum_numbers(x) for x in data)
        elif isinstance(data, dict):
            return sum(sum_numbers(v) for v in data.values())
        else:
            return 0
    
    with open("input_12_01") as f:
        data = json.load(f)
    
    print(sum_numbers(data))
  ```

# This Solves part 01 of the challenge for Day 12
