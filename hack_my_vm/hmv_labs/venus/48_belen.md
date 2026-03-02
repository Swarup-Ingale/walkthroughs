# Target User
leona  -pass: freedom

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- cat the stolen.txt and copy the contents and save it on our local machine
- It is a md5crypt hash with salt leona so lets use john to find the password
  ```
    ┌──(kali㉿kali)-[~/hack_my_vm/hvmlabs/venus]
    └─$ echo '$1$leona$lhWp56YnWAMz6z32Bw53L0' > leona.hash
                                                                                                                                                                                
    ┌──(kali㉿kali)-[~/hack_my_vm/hvmlabs/venus]
    └─$ cat leona.hash                                     
    $1$leona$lhWp56YnWAMz6z32Bw53L0
                                                                                                                                                                                
    ┌──(kali㉿kali)-[~/hack_my_vm/hvmlabs/venus]
    └─$ john --format=md5crypt  -wordlist=/usr/share/wordlists/rockyou.txt leona.hash
    Using default input encoding: UTF-8
    Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 SSE2 4x3])
    Will run 4 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    freedom          (?)     
    1g 0:00:00:00 DONE (2026-03-02 10:25) 5.000g/s 1920p/s 1920c/s 1920C/s alyssa..michael1
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed.
  ```
- The Password is **freedom**

# Commands Used
- ls -la
- cat
- echo
- john
