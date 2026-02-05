# Target User
violet  -pass: a9HFXWKINVzNQLKLDVAc

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list the files in directory and cat the mission.txt
- Find the line that begins with the given text from file passy using the sed command
- Get the password
  ```
    isla@venus:~$ sed -n '/^a9HFX/p' passy
    a9HFXWKINVzNQLKLDVAc
  ```

# Commands Used
- ls -la
- cat
- sed
