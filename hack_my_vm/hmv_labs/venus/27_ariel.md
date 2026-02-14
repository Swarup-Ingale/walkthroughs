# Target User
lola  -pass: d3LieOzRGX5wud6

# Method of Solve
- Login using the given ssh credentials
- perform ls -la to list all the files and cat to read the mission.txt
- use vim -r flag to recover the broken or tainted .goas.swp file
- convert it into strings using the strings command
- Then Remove all the special characters such as arrows to get clean passwords
- Save them on your own machine or system
- Use hydra to crack bruteforce the password for lola
  ```
     hydra -s 5000 -l lola -P passwords_lola.txt venus.hackmyvm.eu ssh
  ```

# Commands Used
- ls -la
- cat
- vim -r
- hydra
