# Targer User
clara  -pass: 39YziWp5gSvgQN9

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- use find command to find the file with -type f and time using -mtime and time
  ```
    eva@venus:~$ find / -type f -mtime +18440 2>/dev/null
    /usr/lib/cmdo
    eva@venus:~$ cat /usr/lib/cmdo 
    39YziWp5gSvgQN9
  ```

# Commands Used
- ls -la
- cat
- find
