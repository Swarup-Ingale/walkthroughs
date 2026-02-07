# Target User
lucy  -pass: OCmMUjebG53giud

# Method of Solve
- Login using the ssh credentials
- perform ls -la to list all the files and cat mission.txt to understand the scope of the challenge
- perform sed command on the end file to get the password
  ```
    violet@venus:~$ sed -n '/0JuAZ$/p' end
    OCmMUjebG53giud0JuAZ
  ```

# Commands Used
- ls -la
- cat
- sed
