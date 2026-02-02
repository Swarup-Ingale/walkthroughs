# URL
https://pwnable.kr/play.php

# SSH COMMAND
ssh random@pwnable.kr -p2222 (pw:guest)

# Source Code
```
  #include <stdio.h>

  int main(){
  	unsigned int random;
  	random = rand();	// random value!
  
  	unsigned int key=0;
  	scanf("%d", &key);
  
  	if( (key ^ random) == 0xcafebabe ){
  		printf("Good!\n");
  		setregid(getegid(), getegid());
  		system("/bin/cat flag");
  		return 0;
  	}
  
  	printf("Wrong, maybe you should try 2^32 cases.\n");
  	return 0;
  }
```

# Concept 
This Challenge teaches us that if we didnt use the functions properly than they are basically useless, as the rand() function is called but srand() is never called and hence the value of generated due to rand() will always be the same which makes it predictable and hence exploitable.

# Method of Solve
- Login into the remote shell using the ssh credentials
- list all the files in the directory to know the files and the permissions provided to the files using "ls -la"
- cat the source code for challenge to see what is going on in the code
- as we can see the rand() function is called but srand() is never called and hence the value of rand() function is not actually random
  ```
    int main(){
  	unsigned int random;
  	random = rand();
  ```
- So now lets try to predict or find the value of returned by the rand()
- For this we will create a new executable c file in /tmp directory
  ```
    random@ubuntu:~$ cd /tmp/
    random@ubuntu:/tmp$ touch abc.c
    random@ubuntu:/tmp$ nano abc.c
  ```
- what code we write in the abc.c :
  ```
    #include <stdio.h>
    #include <stdlib.h>
    
    int main() {
        printf("%u\n", rand());
        return 0;
    }
  ```
- Here we are getting the value returned by the rand()
- Now lets compile it and run it to see what value it reveals:
  ```
    random@ubuntu:/tmp$ gcc abc.c -o abc
    random@ubuntu:/tmp$ ./abc
    1804289383
  ```
- As we can see, we got the value returned by rand()
- Now lets get back to basics as the next part of source code is doing **XOR** of the key we input with the value returned by rand() and comparing it with the hex value **0xcafebabe**
- As we know that :
  ```
    if a ^ b = c
    then a = b ^ c
  ```
- So similarly, here we have:
  ```
    a = key ---> the input we have to give
    b = rand() --> 1804289383
    c = 0xcafebabe
  ```
- Also the Decimal value of **0xcafebabe** is **3405691582**
- So we can apply same logic by using a python script
  ```
    a = 3405691582 # Decimal of 0xcafebabe
    b = 1804289383 # Decimal value returned by the rand()
    # Performing the xor and storing the result in separate variable
    xor = a ^ b
    
    print(xor)
  ```
- Now we got our input to be given as key = "2708864985"
- So now lets run the challenge :
  ```
    random@ubuntu:~$ ./random 
    2708864985
    Good!
    m0mmy_I_can_predict_rand0m_v4lue!
  ```
- And we get the flag and it is **m0mmy_I_can_predict_rand0m_v4lue!**
