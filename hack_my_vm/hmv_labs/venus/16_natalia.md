# Target User
eva  -pass: upsCA3UFu10fDAO

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- cat the base64.txt and decode the base64 encoded password by using python or cyberchef.io
- Get the password
  ```
    natalia@venus:~$ cat base64.txt 
    dXBzQ0EzVUZ1MTBmREFPCg==
    pass : upsCA3UFu10fDAO
  ```
- OR
  ```
   natalia@venus:~$ base64 -d base64.txt
   upsCA3UFu10fDAO
  ```
  
# Commands Used
- ls -la
- cat
- base64
- python
- cyberchef
