# URL
https://adventofcode.com/2017/day/4

# Description
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:
```
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
```
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    valid_count = 0
    
    with open("input_04", "r") as f:
        for line in f:
            words = line.strip().split()
    
            if len(words) == len(set(words)):
                valid_count += 1
    
    print(valid_count)
  ```
- This Solves the Part 01 of this challenge.
