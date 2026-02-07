# Username
bandit3

# Password
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

# Method of Solve
- Login using the ssh credentials
- Perform cd into the inhere directory
- Perform ls -la to list hidden files
  ```
    bandit3@bandit:~/inhere$ ls -la
    total 12
    drwxr-xr-x 2 root    root    4096 Oct 14 09:26 .
    drwxr-xr-x 3 root    root    4096 Oct 14 09:26 ..
    -rw-r----- 1 bandit4 bandit3   33 Oct 14 09:26 ...Hiding-From-You
  ```
- Then Perform cat operation on hidden file
  ```
    bandit3@bandit:~/inhere$ cat ...Hiding-From-You 
    2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
  ```
