# Target User
noa  -pass: 9WWOPoeJrq6ncvJ

# Method of Solve
- Login usinf the ssh credentials
- Perform ls -la to list all the files in the directory and cat mission.txt
- copy the zip.gz file to the /tmp/ directory
- look for its file type using file command
  ```
    lana@venus:/tmp/...swale$ file zip.gz 
    zip.gz: POSIX tar archive (GNU)
  ```
- tar archive so lets use tar to unzip it
  ```
    lana@venus:/tmp/...swale$ tar -xvf zip.gz 
    pwned/lana/zip
  ```
- Then lets cd into the lana directory and cat the password.
- The password is **9WWOPoeJrq6ncvJ**

# Commands Used
- ls -la
- cat
- file
- tar
