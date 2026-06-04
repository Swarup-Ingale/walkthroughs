# URL
https://training.olicyber.it/challenges#challenge-258

# Concept
To understand what are strings present in the elf file and how can we extract those using the strings command.

# Method of Solve
- Navigate to the challenge URL and read the description.
- Download the elf binary attachment.
- use strings command to print all the printable strings present in the elf.
- At the same time use grep to grab only the required string from the noise.
  ```
    strings sw-04 | grep -i "flag"
      flag{0cca06f6}
       la flag? : 
      flag
  ```
- The flag is **flag{0cca06f6}**
