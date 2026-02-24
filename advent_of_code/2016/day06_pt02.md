# URL
https://adventofcode.com/2016/day/6#part2

# Description
Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
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
        most_common_char = Counter(column_chars).most_common()[-1][0]
        message.append(most_common_char)
    
    # Final corrected message
    print("Error-corrected message:", "".join(message))
  ```

# This Concludes the Day 06 of The Advent of Code.
