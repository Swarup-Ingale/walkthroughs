# URL
https://pwnable.kr/play.php

# SSH COMMAND
ssh fd@pwnable.kr -p2222 (pw:guest)

# Source Code
  ```
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    char buf[32];
    int main(int argc, char* argv[], char* envp[]){
    	if(argc<2){
    		printf("pass argv[1] a number\n");
    		return 0;
    	}
    	int fd = atoi( argv[1] ) - 0x1234;
    	int len = 0;
    	len = read(fd, buf, 32);
    	if(!strcmp("LETMEWIN\n", buf)){
    		printf("good job :)\n");
    		setregid(getegid(), getegid());
    		system("/bin/cat flag");
    		exit(0);
    	}
    	printf("learn about Linux file IO\n");
    	return 0;
    }

  ```

# Concept
To Learn about what are linux(unix) file descriptors (fd) and how they work 
such as "0" represents stdin "1" represent stdout and "2" represents stderror

# Method of Solve
- first login using the ssh credentials
- then look for all the files in the directory you are in using ls -la
- then look for fd.c and cat it
- try to understand what the code actually does
    ```
      char buf[32];
      int main(int argc, char* argv[], char* envp[]){
      	if(argc<2){
      		printf("pass argv[1] a number\n");
      		return 0;
      	}
    ```
- Here we are creating a buffer of size 32 bytes and then passing an number as a argument to the fd file
- then move on to the next part
    ```
      int fd = atoi( argv[1] ) - 0x1234;
    	int len = 0;
    	len = read(fd, buf, 32);
    	if(!strcmp("LETMEWIN\n", buf)){
    		printf("good job :)\n");
    		setregid(getegid(), getegid());
    		system("/bin/cat flag");
    		exit(0);
    	}
    	printf("learn about Linux file IO\n");
    	return 0;
      }
    ```
- Here we are setting fd variable to input argument - 0x1234
- 0x1234 is 4660 in decimal and so we have to make the fd as "0" in order to perform stdin or input something in thw buffer
- then we perfrom read on the fd (which should be 0), buff which is set as 32 bytes and size or count of characters (which is again 32)
- then we compare our input into the buffer with string "LETMEWIN", if it matches we get the flag
- so the input for fd as argument will be **4660** as 4660 - 4660 = 0 which is fd for stdin
- and then we will input LETMEWIN string into the buffer and get the flag
    ```
      fd@ubuntu:~$ ./fd 4660
                    LETMEWIN
                    good job :)
                    Mama! Now_I_understand_what_file_descriptors_are!
    ```
- The Solution Flag is : **Mama! Now_I_understand_what_file_descriptors_are!**
