# Target User
eliza  -pass: Fg6b6aoksceQqB9

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list the files and cat the mission.txt
- Now to perform uniqueness check and find repreated strings we use uniq command
  ```
    frida@venus:~$ uniq -c repeated.txt | sort
    1 aahskaskjskasjk
    .
    .
    .
    .
    2 Fg6b6aoksceQqB9
  ```
- We get the password

# Commands Used
- ls -la
- cat
- uniq
