# Target User
eloise  -pass: yOUJlV0SHOnbSPm

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Copy the eliose file ccontents in the local machine and save it as filename.b64 as it is a base64 file
- Then decode the base64 and save it as jpg file as the file contents after decoding gives the magic numbers of a JPEG file
  ```
    base64 -d eliose.b64 > eliose.jpg
  ```
- Then open the jpg file and read the password

# Commands Used
- ls -la
- cat
- base64
- file
