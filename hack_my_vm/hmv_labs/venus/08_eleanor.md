# Target User
victoria  -pass: pz8OqvJBFxH0cSj

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list the files in the directory
- cat the mission.txt and perform find command to find the specified file
- Get the password from that file
  ```
    eleanor@venus:~$ find / -user violin -type f 2> /dev/null 
    /usr/local/games/yo
    eleanor@venus:~$ cd /usr/local/games/yo
    bash: cd: /usr/local/games/yo: Not a directory
    eleanor@venus:~$ cat /usr/local/games/yo
    pz8OqvJBFxH0cSj
  ```

# Commands Used
- ls -la
- cat
- find
