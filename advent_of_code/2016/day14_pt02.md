# URL
https://adventofcode.com/2016/day/14#part2

# Description
Of course, in order to make this process even more secure, you've also implemented key stretching.

Key stretching forces attackers to spend more time generating hashes. Unfortunately, it forces everyone else to spend more time, too.

To implement key stretching, whenever you generate a hash, before you use it, you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. Always use lowercase hexadecimal representations of hashes.

For example, to find the stretched hash for index 0 and salt abc:
```
Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
...repeat many times...
Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.
```
So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:
```
The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.
```
Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    import hashlib
    
    def stretched_md5(s):
        # First hash
        h = hashlib.md5(s.encode()).hexdigest()
        
        # 2016 additional hashes (total 2017)
        for _ in range(2016):
            h = hashlib.md5(h.encode()).hexdigest()
        
        return h
    
    
    def first_triplet(h):
        for i in range(len(h) - 2):
            if h[i] == h[i+1] == h[i+2]:
                return h[i]
        return None
    
    
    def find_64th_key_part2(filename):
       
        with open(filename, "r") as f:
            salt = f.read().strip()
    
        index = 0
        keys_found = 0
        hash_cache = {}
    
        while True:
            # Compute or reuse stretched hash
            if index not in hash_cache:
                hash_cache[index] = stretched_md5(salt + str(index))
    
            current_hash = hash_cache[index]
            triplet_char = first_triplet(current_hash)
    
            if triplet_char:
                quintuple = triplet_char * 5
    
                # Look ahead 1000 hashes
                for future_index in range(index + 1, index + 1001):
                    if future_index not in hash_cache:
                        hash_cache[future_index] = stretched_md5(salt + str(future_index))
    
                    if quintuple in hash_cache[future_index]:
                        keys_found += 1
                        print(f"Key {keys_found} found at index {index}")
                        break
    
                if keys_found == 64:
                    return index
    
            index += 1
    
    result = find_64th_key_part2("input_14")
    print("Index of 64th key (Part 2):", result)
  ```

# This Concludes the Day 14 of The Advent of Code.
