# Target User
zora   -pass: BWm1R3jCcb53riO

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- doas is a special config file which helps us execute certain commands as other users
- lets use doas to get access of zora
  ```
    denise@venus:~$ doas -su zora
    doas (denise@venus) password: 
    
    doas: Authentication failed
  ```
- Here we feed the denise password to login as zora
- The Password for zora is **BWm1R3jCcb53riO**

# Commands Used
- ls -la
- cat
- su
- doas
