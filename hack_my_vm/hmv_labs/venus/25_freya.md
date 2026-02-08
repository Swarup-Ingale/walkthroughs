# Target User
alexa  -pass: mxq9O3MSxxX9Q3S

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Now since the user creates a file with .txt extension in every 1 minute and deletes it quickly Lets create a script for monitoring the directory continuously and cat the file as soon as it appears
  ```
    freya@venus:/free$ while true; do [ -f /free/* ] && cat /free/*; sleep 1; done
    mxq9O3MSxxX9Q3S
  ```

# Commands Used
- ls -la
- cat
- bash scripting 
