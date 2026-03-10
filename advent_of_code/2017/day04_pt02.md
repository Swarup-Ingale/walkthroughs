# URL
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:
```
abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
```
Under this new system policy, how many passphrases are valid?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
  ```
    valid_count = 0
    
    with open("input_04", "r") as f:
        for line in f:
            words = line.strip().split()
    
            # Normalize words by sorting letters
            normalized = [''.join(sorted(word)) for word in words]
    
            # Check for duplicates after normalization
            if len(normalized) == len(set(normalized)):
                valid_count += 1
    
    print(valid_count)
  ```

# This Solves Day 04 of The Advent of Code.
