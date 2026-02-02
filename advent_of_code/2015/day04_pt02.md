# URL
https://adventofcode.com/2015/day/4#part2

# Description
Now find one that starts with six zeroes.

# Method of Solve
The below given code solves the Part 02 of this Challenge:
  ```
    import hashlib
    with open("input_04_01", 'r') as INPUT:
    	advent_coin = INPUT.read().strip()
    
    n=1
    
    while True:
        data = advent_coin + str(n)
        md5_hash = hashlib.md5(data.encode()).hexdigest()
    
        if md5_hash.startswith("000000"):
            print(n)
            break
    
        n += 1
  ```
This concludes day 04 challenge of advent of code
