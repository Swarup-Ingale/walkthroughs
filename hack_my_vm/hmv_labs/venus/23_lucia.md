# Target User
isabel  -pass: H5ol8Z2mrRsorC0

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list the files and cat the mission.txt
- craft a script for getting the readable file from the given directory and get the password
  ```
    lucia@venus:~$ cat dict.txt | xargs -I {} sh -c 'if [ -r /etc/xdg/{} ]; then echo "Readable file found /etc/xdg/{}"; exit 0; fi' || echo "No Readable File found in /etc/xdg/ directory"
    Readable file found /etc/xdg/readme
  ```
- Then cat the readme file to get password
  ```
    lucia@venus:~$ cat /etc/xdg/readme
    H5ol8Z2mrRsorC0
  ```

# Commands Used
- ls -la
- cat
- xargs
- echo
