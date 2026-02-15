# URL
https://training.olicyber.it/challenges#challenge-326

# Concept
To Understand Encoding and types of encodings, how to identify them and how to decode them 

# Method of Solve
- Go to the Challenge URL and copy the encoded value
- We will use python to decode the Ascii encoded flag and get the flag
- The python script is :
  ```
    nums = [102,108,97,103,123,117,103,104,95,78,117,109,66,51,114,53,95,52,49,114,51,52,100,121,125]
    print("".join(chr(n) for n in nums))
  ```
- The flag is **flag{ugh_NumB3r5_41r34dy}**
