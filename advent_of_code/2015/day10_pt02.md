# URL
https://adventofcode.com/2015/day/10#part2

# Description
Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

# Method of Solve
- The below given code solves the part 02 of the challenge
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
    
    for _ in range(50):
        s = look_and_say(s)
    
    print(len(s))
  ```
- The code is just same as the part 01 only the count has changed from 40 to 50

# This concludes the Day 10 of the Advent of Code
