# URL
https://adventofcode.com/2015/day/10

# Description
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:
```
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
```
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# Method of Solve
- The Solution for part 01 of the challenge can be obtained using the code given below
  ```
    def look_and_say(s):
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1

    
    result.append(str(count))
    result.append(s[-1])

    return ''.join(result)


    with open("input_10_01", "r") as f:
        s = f.read().strip()
    
    for _ in range(40):
        s = look_and_say(s)
    
    print(len(s))
  ```

# This Solves the part 01 of day 10
