# URL
https://adventofcode.com/2015/day/4

# Description
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:
```
If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
```
Your puzzle input is ********.

# Method of Solve
The Following code Solves the part 01 of the Challenge:
  ```
    import hashlib
    with open("input_04_01", 'r') as INPUT:
    	advent_coin = INPUT.read().strip()
    
    n=1
    
    while True:
        data = advent_coin + str(n)
        md5_hash = hashlib.md5(data.encode()).hexdigest()
    
        if md5_hash.startswith("00000"):
            print(n)
            break
    
        n += 1
  ```
This code solves the part 01 of the challenge for day 04
