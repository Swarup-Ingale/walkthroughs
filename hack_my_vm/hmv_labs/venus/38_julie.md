# Target User
irene  -pass: 8VeRLEFkBpe2DSD

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- we are provided with 1.txt and 2.txt and hinted towards the difference
- So now lets use the diff command to find the passwowrds or strings that are different among the two files
  ```
    julie@venus:~$ diff 1.txt 2.txt 
    174c174
    < 8VeRLEFkBpe2DSD
    ---
    > aNHRdohjOiNizlU
  ```
- The Password is **8VeRLEFkBpe2DSD**

# Commands Used
- ls -la
- cat
- diff
