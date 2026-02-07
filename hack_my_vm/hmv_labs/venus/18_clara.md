# Target User
frida  -pass: Ed4ErEUJEaMcXli

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Now to get the password protected zip file into our machine lets use scp command
  ```
    scp -P 5000 clara@venus.hackmyvm.eu:~/protected.zip .
  ```
- Then convert it into a john understandable zip
  ```
    zip2john protected.zip > fridahash
  ```
- Then lets use bruteforcing using john to crack the password of the zip file
  ```
    john fridahash --wordlist=/home/kali/rockyou.txt
  ```
- Finally use the password to unzip the file and hence read the password using cat
  ```
    └─$ unzip protected.zip
    Archive:  protected.zip
    [protected.zip] pwned/clara/protected.txt password: 
     extracting: pwned/clara/protected.txt
  ```
- And now cat the protected.txt file
  ```
    └─$ cat pwned/clara/protected.txt 
    Ed4ErEUJEaMcXli
  ```

# Commands Used
- ls -la
- cat
- john (tool)
- unzip
- scp
