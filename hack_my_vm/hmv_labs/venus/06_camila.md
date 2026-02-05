# Target User
luna  -pass: j3vkuoKQwvbhkMc

# Method of Solve
- Login using the ssh credentials
- Perform ls -la for listing all the files in the directory and cat the mission.txt
- Perform find command to fing the file in which password is stored
- Get the flag
  ```
    camila@venus:~$ find muack -type f | xargs file
    muack/111/111/muack: ASCII text
    camila@venus:~$ cat muack/111/111/muack
    j3vkuoKQwvbhkMc
  ```

# Commands Used
- ls -la
- cat
- find
