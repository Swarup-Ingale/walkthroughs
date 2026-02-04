# Target User
angela  -pass: oh5p9gAABugHBje

# Method of Solve
- login using the ssh credentials
- perform ls -la to list all the files in the directory and cat the mission.txt
- use find command to find the password file for angela
  ```
    sophia@venus:~$ find / -name whereismypazz.txt 2>/dev/null
    /usr/share/whereismypazz.txt
    sophia@venus:~$ cat /usr/share/whereismypazz.txt 
    oh5p9gAABugHBje
    sophia@venus:~$ su angela
    Password: 
    GOGETA SSJ1!
    tornillo paso 2 XP
  ```

  # Tools Used
  - ls -la
  - cat
  - su
  - find
