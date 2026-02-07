# Target User
elena  -pass: 4xZ5lIKYmfPLg9t

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Perform sed command on the file.yo to match the exact regex to get the password
  ```
    lucy@venus:~$ sed -n 's/.*fu\([^<]*\)ck.*/\1/p' file.yo
    4xZ5lIKYmfPLg9t
  ```

# Commands Used
- ls -la
- cat
- sed
