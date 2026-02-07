# Target User
anna  -pass: w8NvY27qkpdePox

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Perform cut operation to get only the required columns and match the username to anna and get the password of anna
  ```
    alice@venus:~$ cut -d: -f1,5 /etc/passwd | grep alice
    alice:w8NvY27qkpdePox
  ```

# Commands Used
- ls -la
- cat
- cut
