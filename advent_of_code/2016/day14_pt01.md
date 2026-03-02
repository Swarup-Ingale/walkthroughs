# URL
https://adventofcode.com/2016/day/14

# Description
In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:
```
The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
Eventually, index 22728 meets all of the criteria to generate the 64th key.
So, using our example salt of abc, index 22728 produces the 64th key.
```
Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?


# Method of Solve
- The part 01 of this challenge can be solved using the following code:
  ```
    import hashlib
    
    def get_md5(s):
        return hashlib.md5(s.encode()).hexdigest()
    
    def find_first_triplet(hash_str):
        for i in range(len(hash_str) - 2):
            if hash_str[i] == hash_str[i+1] == hash_str[i+2]:
                return hash_str[i]
        return None
    
    def find_64th_key(filename):
        # Read salt using open()
        with open(filename, "r") as f:
            salt = f.read().strip()
    
        index = 0
        keys_found = 0
        hash_cache = {}
    
        while True:
            # Compute or retrieve hash
            if index not in hash_cache:
                hash_cache[index] = get_md5(salt + str(index))
    
            current_hash = hash_cache[index]
            triplet_char = find_first_triplet(current_hash)
    
            if triplet_char:
                quintuple = triplet_char * 5
    
                # Look ahead 1000 hashes
                for future_index in range(index + 1, index + 1001):
                    if future_index not in hash_cache:
                        hash_cache[future_index] = get_md5(salt + str(future_index))
    
                    if quintuple in hash_cache[future_index]:
                        keys_found += 1
                        print(f"Key {keys_found} found at index {index}")
                        break
    
                if keys_found == 64:
                    return index
    
            index += 1
    
    
    result = find_64th_key("input_14")
    print("Index of 64th key:", result)
  ```
- This Solves the part 01 of this challenge.
