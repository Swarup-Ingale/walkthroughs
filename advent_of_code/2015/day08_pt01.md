# URL 
https://adventofcode.com/2015/day/8

# Description
Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:
```
"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
```
Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example:
```
given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
```

# Method of Solve
- The Part 01 of the challenge can be solved using the code given below:
  ```
    def memory_length(s):
      i = 1  				# skip opening quote
      mem = 0
      while i < len(s) - 1:  		# skip closing quote
          if s[i] == '\\':
              if s[i+1] in ['\\', '"']:
                  mem += 1
                  i += 2
              elif s[i+1] == 'x':
                  mem += 1
                  i += 4  		# \xTWOBYTES FOR HEX
          else:
              mem += 1
              i += 1
      return mem
  
  
    total_code_storage = 0
    total_mem_storage = 0
    
    with open("input_08_01") as f:
        for line in f:
            line = line.strip()
            total_code_storage += len(line)
            total_mem_storage += memory_length(line)
    
    print(total_code_storage - total_mem_storage)
  ```

# This Solves the Part 01 of the challenge.
