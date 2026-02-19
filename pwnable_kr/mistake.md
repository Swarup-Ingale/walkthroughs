# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh mistake@pwnable.kr -p2222 (pw:guest)

# Source Code
  ```
    #include <stdio.h>
    #include <fcntl.h>
    
    #define PW_LEN 10
    #define XORKEY 1
    
    void xor(char* s, int len){
    	int i;
    	for(i=0; i<len; i++){
    		s[i] ^= XORKEY;
    	}
    }
    
    int main(int argc, char* argv[]){
    	
    	int fd;
    	if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
    		printf("can't open password %d\n", fd);
    		return 0;
    	}
    
    	printf("do not bruteforce...\n");
    	sleep(time(0)%20);
    
    	char pw_buf[PW_LEN+1];
    	int len;
    	if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
    		printf("read error\n");
    		close(fd);
    		return 0;		
    	}
    
    	char pw_buf2[PW_LEN+1];
    	printf("input password : ");
    	scanf("%10s", pw_buf2);
    
    	// xor your input
    	xor(pw_buf2, 10);
    
    	if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
    		printf("Password OK\n");
    		setregid(getegid(), getegid());
    		system("/bin/cat flag\n");
    	}
    	else{
    		printf("Wrong Password\n");
    	}
    
    	close(fd);
    	return 0;
    }
  ```

# Concept
To Understand how a simple Mistake in logic even a paranthesis logic can make the entire code vulnerable.

# Method of Solve
- Go to the Challenge URL and Login using the ssh credentials
- Read and understand the source code.
- In the source code, we first perform xor of password01 with KEY 1 both are in hex.
  ```
    void xor(char* s, int len){
    	int i;
    	for(i=0; i<len; i++){
    		s[i] ^= XORKEY;
    	}
    }
  ```
- Then we are taking password02 as input and checking our output with the XOR value of password01.
  ```
    char pw_buf[PW_LEN+1];
  	int len;
  	if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
  		printf("read error\n");
  		close(fd);
  		return 0;		
  	}
  
  	char pw_buf2[PW_LEN+1];
  	printf("input password : ");
  	scanf("%10s", pw_buf2);
  
  	// xor your input
  	xor(pw_buf2, 10);
  
  	if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
  		printf("Password OK\n");
  		setregid(getegid(), getegid());
  		system("/bin/cat flag\n");
  	}
  	else{
  		printf("Wrong Password\n");
  	}
  ```
- Then once the both match we get our flag printed as output.
- The flaw is in the logic of handling **fd** in the line:
  ```
    int fd;
  	if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
  		printf("can't open password %d\n", fd);
  		return 0;
  	}
  ```
- Due to this the value of fd is stored instead of password .... which is later on compared.
- Eg, If we input password01 as **AAAAAAAAAA** (since buffer Sixe is 10).
- And then password02 as **@@@@@@@@@@** (Since buffer size is 10).
- The hex value of **A** is **41** and **41 ^ 1** is **50** which is then added with 1.
- That makes it **51** which is when XOR again with 1 gives **40** which is **@**.
- And hence if password01 is **AAAAAAAAAA** then password02 should be **@@@@@@@@@@** due to comparission logic.
  ```
    mistake@ubuntu:~$ ./mistake 
    do not bruteforce...
    AAAAAAAAAA
    
    input password : @@@@@@@@@@
    Password OK
    Mommy_the_0perator_priority_confuses_me
  ```
- The Flag is **Mommy_the_0perator_priority_confuses_me**
