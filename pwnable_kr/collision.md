# URL
https://pwnable.kr/play.php

# SSH COMMAND
ssh col@pwnable.kr -p2222 (pw:guest)

# Source Code
  ```
    #include <stdio.h>
    #include <string.h>
    unsigned long hashcode = 0x21DD09EC;
    unsigned long check_password(const char* p){
    	int* ip = (int*)p;
    	int i;
    	int res=0;
    	for(i=0; i<5; i++){
    		res += ip[i];
    	}
    	return res;
    }
    
    int main(int argc, char* argv[]){
    	if(argc<2){
    		printf("usage : %s [passcode]\n", argv[0]);
    		return 0;
    	}
    	if(strlen(argv[1]) != 20){
    		printf("passcode length should be 20 bytes\n");
    		return 0;
    	}
    
    	if(hashcode == check_password( argv[1] )){
    		setregid(getegid(), getegid());
    		system("/bin/cat flag");
    		return 0;
    	}
    	else
    		printf("wrong passcode.\n");
    	return 0;
    }
  ```

# Concept
Learn about what are hashes and how Hash Collision occurs and what can we so using Hash Collisions (here **MD5**)

# Method of Solve
- login using the ssh credentials
- perform listing of all the files and folders present in the directory using ls -la
- look for yhe col.c file and cat it to study and understand what its doing
  ```
    int main(int argc, char* argv[]){
  	if(argc<2){
  		printf("usage : %s [passcode]\n", argv[0]);
  		return 0;
  	}
  	if(strlen(argv[1]) != 20){
  		printf("passcode length should be 20 bytes\n");
  		return 0;
  	}
  ```
- here we are taking argument as string and checking if its length is 20 bytes ...
- if yes then furthur code will be executed or else it will print "Passcode length should be 20 bytes"
- next
    ```
      if(hashcode == check_password( argv[1] )){
  		setregid(getegid(), getegid());
  		system("/bin/cat flag");
  		return 0;
    	}
    	else
    		printf("wrong passcode.\n");
    	return 0;
      }
    ```
- Here we are checking our entered argument with hashcode after passing the argument through check_pasword() function
- If it matches we get flag
- The check_password() function
  ```
    unsigned long hashcode = 0x21DD09EC;
    unsigned long check_password(const char* p){
    	int* ip = (int*)p;
    	int i;
    	int res=0;
    	for(i=0; i<5; i++){
    		res += ip[i];
    	}
    	return res;
    }
  ```
- Here now the hashcode is set as "0x21DD09EC" and we are taking the char at from argument at pointer p and storing it at pointer ip after typecasting it into int
- then we are running the 4 bytes "0x21DD09EC" 5 times and storing it in res after doing res = res + ip[i] to make it 20 Bytes Long valid string
- this satifies the 20 Bytes or 20 characters long condition
  ```
    col@ubuntu:~$ ./col $'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xe8\x05\xd9\x1d'
                  Two_hash_collision_Nicely
  ```
- The flag is : **Two_hash_collision_Nicely**
