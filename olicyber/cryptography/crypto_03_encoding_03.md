# URL
https://training.olicyber.it/challenges#challenge-328

# Concept
To Understand about Endians (Little and Big : For more info look the security research notes) and how to decode and perform interconversion in them.

# Method of Solve
- Go to the Challenge URL and copy the encoded values of flag
- Write a Script in python to decode it...
  ```
    import base64

    part1_b64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
    
    part1 = base64.b64decode(part1_b64).decode()
    
    print("Part 1 decoded:", part1)
    
    number = 664813035583918006462745898431981286737635929725
    
    num_bytes = (number.bit_length() + 7) // 8
    
    part2_bytes = number.to_bytes(num_bytes, byteorder="big")
    
    part2 = part2_bytes.decode()
    
    print("Part 2 decoded:", part2)
    
    # FLAG 
    flag = part1 + part2
    print("\nFinal Flag:", flag)
  ```
- First we decode the base64 directly with the help of the base64 library or module of python
- Then we calculate the length of the Bytes of the part 02 of the flag
- Then we identify the Endian type of the encoded value (here Big)
- Then we finally decode it by Using the number to bytes function
- The flag is **flag{w41t_1ts_all_b1ts?_4lw4ys_H4s_b33n}**
