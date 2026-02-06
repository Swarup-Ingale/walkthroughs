# URL
https://adventofcode.com/2015/day/12#part2

# Description
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).
```
[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.
```

# Method of Solve
- The code to solve the part 02 of the challenge is as follows:
  ```
    import json

    def sum_numbers(data):
        if isinstance(data, int):
            return data
    
        elif isinstance(data, list):
            return sum(sum_numbers(item) for item in data)
    
        elif isinstance(data, dict):
            # ignore object if any value is "red"
            if "red" in data.values():
                return 0
            return sum(sum_numbers(value) for value in data.values())
    
        return 0
    
    
    with open("input_12_01", "r") as f:
        data = json.load(f)
    
    print(sum_numbers(data))
  ```

# This Concludes the Day 12 of The Advent of Code
