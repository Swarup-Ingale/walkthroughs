# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh cmd2@pwnable.kr -p2222 (pw:flag of cmd1)

# Source Code
  ```
    #include <stdio.h>
    #include <string.h>
    
    int filter(char* cmd){
    	int r=0;
    	r += strstr(cmd, "=")!=0;
    	r += strstr(cmd, "PATH")!=0;
    	r += strstr(cmd, "export")!=0;
    	r += strstr(cmd, "/")!=0;
    	r += strstr(cmd, "`")!=0;
    	r += strstr(cmd, "flag")!=0;
    	return r;
    }
    
    extern char** environ;
    void delete_env(){
    	char** p;
    	for(p=environ; *p; p++)	memset(*p, 0, strlen(*p));
    }
    
    int main(int argc, char* argv[], char** envp){
    	delete_env();
    	putenv("PATH=/no_command_execution_until_you_become_a_hacker");
    	if(filter(argv[1])) return 0;
    	printf("%s\n", argv[1]);
    	setregid(getegid(), getegid());
    	system( argv[1] );
    	return 0;
    }
  ```

# Concept 
The concept behind this challenge is Restricted Shell Environment Injection. The program tries to create a "sandbox" by clearing all environment variables and filtering specific characters, but it fails because it passes our input directly to system(), which triggers a full shell (/bin/sh or /bin/bash).

Since the shell interprets our input before executing it, we can use Command Substitution and Internal Globbing to rebuild the forbidden strings.

# Method of Solve
- Login using the SSH Credentials and read the provided C code .. cmd2.c
- Now we first used the shells built-ins such as echo, read so that the system does not require any PATH specified for it
- Then we have to bypass the = filter.
- This can be done using the mechanisms that set variables without using an equals sign, eg : read
- Then we can use the wildcard execution * to bypass the filter of flag file
- Here I used printf as shell variable and for */* bypass I used its hex equivalent **\57** also to bypass the flag file filter I used the **?** operator to complete only required characters in the file instead of wildcard.
- The Final Payload is :
  ```
    ./cmd2 '$(printf "\57")bin$(printf "\57")cat fl??'
  ```
- The Flag is **Shell_variables_can_be_quite_fun_to_play_with!**
