# URL
https://adventofcode.com/2016/day/6

# Description
Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:
```
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
```
The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

# Method of Solve
- The part 01 of this challenge can be solved using the following code:
  ```
    from collections import Counter
    
    with open("input_06", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    # Number of characters per line
    length = len(lines[0])
    
    message = []
    
    # Process column by column
    for i in range(length):
        column_chars = [line[i] for line in lines]
        most_common_char = Counter(column_chars).most_common(1)[0][0]
        message.append(most_common_char)
    
    # Final corrected message
    print("Error-corrected message:", "".join(message))
  ```
- This solves the part 01 of the challenge.
