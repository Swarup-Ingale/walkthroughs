# URL
https://training.olicyber.it/challenges#challenge-255

# Concept
To understand how to look for the binary compiled architechture of te ELF file using the file command.

# Method of Solve
- Navigate to the challenge URL and read it.
- Download the attachment file.
- Analyze it using the file command to get the architechture.
  ```
    file sw-01                                                    
    sw-01: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), statically linked, BuildID[sha1]=0073012c38af01374a53569a0d79290259d34d8d, not stripped
  ```
- The flag is **flag{aarch64}**
