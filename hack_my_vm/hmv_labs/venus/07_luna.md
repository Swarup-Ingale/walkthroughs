# Target User
eleanor  -pass: UNDchvln6Bmtu7b

# Method of Solve
- Login using the ssh credentials
- perform ls -la to list all the files in directory and cat the mission.txt
- Perform find command to find the file with 6969 bytes
- Get the password from that file
  ```
    luna@venus:~$ find / -type f -size 6969c 2>/dev/null
    /usr/share/moon.txt
    luna@venus:~$ cat /usr/share/moon.txt
    UNDchvln6Bmtu7b
  ```

# Commands Used
- ls -la
- cat
- find
