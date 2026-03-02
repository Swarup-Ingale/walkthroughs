# Target User
karla  -pass: gYAmvWY3I7yDKRf

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Using groups commands lets find which group karla belongs to
  ```
    paula@venus:~$ groups karla
    karla : karla
  ```
- Then lets look for our id
  ```
    paula@venus:~$ id
    uid=1044(paula) gid=1044(paula) groups=1044(paula),1053(hidden)
  ```
- Now as we can see the karla group is hidden or owned by the hidden group which share files between paula and karla
- So now lets find a file with group attribute or owned by group hidden
  ```
    paula@venus:~$ find / -group hidden 2>/dev/null 
    /usr/src/.karl-a
  ```
- Now Lets cat the file to get the password
  ```
    paula@venus:/usr/src$ ls -la
    total 16
    drwxr-xr-x 1 root root   4096 Apr  5  2024 .
    drwxr-xr-x 1 root root   4096 Mar 11  2024 ..
    -rw-r----- 1 root hidden   16 Apr  5  2024 .karl-a
    paula@venus:/usr/src$ cat .karl-a 
    gYAmvWY3I7yDKRf
  ```
- The Password is **gYAmvWY3I7yDKRf**

# Commands Used
- ls -la
- cat
- groups
- id
- find
