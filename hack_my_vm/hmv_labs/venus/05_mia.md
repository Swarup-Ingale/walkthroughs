# Target User
camila  -pass: F67aDmCAAgOOaOc

# Method of Solve
- Login using the ssh credentials
- perform ls -la and read the mission.txt using the cat command
- perform find operation to find the directory
- ls -la the directory to look for the files
- cat the .here file to get the credentials
  ```
    mia@venus:~$ find / -type d -name hereiam 2>/dev/null
    /opt/hereiam
    mia@venus:~$ cd /opt/
    mia@venus:/opt$ cd hereiam/ 
    mia@venus:/opt/hereiam$ ls -la
    total 12
    drwxr-xr-x 2 root root 4096 Apr  5  2024 .
    drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
    -rw-r--r-- 1 root root   16 Apr  5  2024 .here
    mia@venus:/opt/hereiam$ cat .here 
    F67aDmCAAgOOaOc
  ```

# Commands Used
- ls -la
- cat
- find
