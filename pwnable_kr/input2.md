# URL
https://pwnable.kr/play.php

# SSH Command
ssh input2@pwnable.kr -p2222 (pw:guest)

# Source Code
```
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  #include <sys/socket.h>
  #include <arpa/inet.h>
  
  int main(int argc, char* argv[], char* envp[]){
  	printf("Welcome to pwnable.kr\n");
  	printf("Let's see if you know how to give input to program\n");
  	printf("Just give me correct inputs then you will get the flag :)\n");
  
  	// argv
  	if(argc != 100) return 0;
  	if(strcmp(argv['A'],"\x00")) return 0;
  	if(strcmp(argv['B'],"\x20\x0a\x0d")) return 0;
  	printf("Stage 1 clear!\n");	
  
  	// stdio
  	char buf[4];
  	read(0, buf, 4);
  	if(memcmp(buf, "\x00\x0a\x00\xff", 4)) return 0;
  	read(2, buf, 4);
          if(memcmp(buf, "\x00\x0a\x02\xff", 4)) return 0;
  	printf("Stage 2 clear!\n");
  	
  	// env
  	if(strcmp("\xca\xfe\xba\xbe", getenv("\xde\xad\xbe\xef"))) return 0;
  	printf("Stage 3 clear!\n");
  
  	// file
  	FILE* fp = fopen("\x0a", "r");
  	if(!fp) return 0;
  	if( fread(buf, 4, 1, fp)!=1 ) return 0;
  	if( memcmp(buf, "\x00\x00\x00\x00", 4) ) return 0;
  	fclose(fp);
  	printf("Stage 4 clear!\n");	
  
  	// network
  	int sd, cd;
  	struct sockaddr_in saddr, caddr;
  	sd = socket(AF_INET, SOCK_STREAM, 0);
  	if(sd == -1){
  		printf("socket error, tell admin\n");
  		return 0;
  	}
  	saddr.sin_family = AF_INET;
  	saddr.sin_addr.s_addr = INADDR_ANY;
  	saddr.sin_port = htons( atoi(argv['C']) );
  	if(bind(sd, (struct sockaddr*)&saddr, sizeof(saddr)) < 0){
  		printf("bind error, use another port\n");
      		return 1;
  	}
  	listen(sd, 1);
  	int c = sizeof(struct sockaddr_in);
  	cd = accept(sd, (struct sockaddr *)&caddr, (socklen_t*)&c);
  	if(cd < 0){
  		printf("accept error, tell admin\n");
  		return 0;
  	}
  	if( recv(cd, buf, 4, 0) != 4 ) return 0;
  	if(memcmp(buf, "\xde\xad\xbe\xef", 4)) return 0;
  	printf("Stage 5 clear!\n");
  
  	// here's your flag
  	setregid(getegid(), getegid());
  	system("/bin/cat flag");	
  	return 0;
  }
```

# Concept 
This challenge tests understanding of **all possible input channels** to a Linux program.  
The binary validates inputs from:

- Command-line arguments (`argv`)
- Standard input (`stdin`)
- Standard error (`stderr`)
- Environment variables
- Filesystem
- Network sockets

# Method of Solve
- We are going to solve this in 5 stages as follows :

### Stage 1 — Command-Line Arguments (`argv`)

**Requirements:**
- Total argument count (`argc`) must be exactly **100**
- `argv[65]` (ASCII `'A'`) must be a **NULL byte**
- `argv[66]` (ASCII `'B'`) must be the byte sequence:
0x20 0x0a 0x0d

- `argv[67]` (ASCII `'C'`) must be a **valid TCP port number**

**Method:**
- Use a scripting language that supports **raw byte arguments**
- Populate unused arguments with dummy values
- Carefully overwrite only the required indexes

### Stage 2 — Standard I/O (stdin and stderr)

**Requirements:**
- stdin (fd 0) must receive:
```
00 0a 00 ff
```
- stderr (fd 2) must receive:
```
00 0a 02 ff
```
**Method:**
- Create pipes
- Write required byte sequences
- Redirect pipes to file descriptors 0 and 2 before execution

### Stage 3 — Environment Variables

**Requirements:**
- Environment variable name:
```
0xde 0xad 0xbe 0xef
```
- Environment variable value:
```
0xca 0xfe 0xba 0xbe
```
**Method:**
- Use a low-level process execution function
- Pass environment variables as raw byte mappings

### Stage 4 — File Input

**Requirements:**
- File name must be a single newline character:
```
"\n"
```
- File content must be exactly:
```
00 00 00 00
```
**Method:**
- Create a file with a newline as its name
- Write four null bytes into it

### Stage 5 — Network Input

**Requirements:**
- Program listens on port provided via argv[67]
- Client must connect and send:
```
de ad be ef
```
**Method:**
- After launching the binary, connect to the listening socket
- Send the required 4-byte sequence

- So the Script is :

```
  from pwn import *
  import os
  
  argv = [str(i) for i in range(0, 100)]
  
  argv[65] = b'\x00'
  argv[66] = b'\x20\x0a\x0d'
  argv[67] = '4444'
  
  r1, w1 = os.pipe()
  r2, w2 = os.pipe()
  
  os.write(w1, b'\x00\x0a\x00\xff')
  os.write(w2, b'\x00\x0a\x02\xff')
  
  with open("\x0a", 'w') as f:
      f.write("\x00\x00\x00\x00")
  
  io = process(executable = '/home/input2/input2', argv = argv, stdin=r1, stderr=r2, env={"\xde\xad\xbe\xef":"\xca\xfe\xba\xbe"})
  
  s = remote('localhost', 4444)
  s.sendline(b"\xde\xad\xbe\xef")
  
  io.interactive()
```
- we have to create the exploit.py in /tmp folder and also run it from the /tmp folder as the home directory is not giving permissions
```
  input2@ubuntu:/tmp$ python /tmp/input2.py
  sys:1: BytesWarning: Text is not bytes; assuming ISO-8859-1, no guarantees. See https://docs.pwntools.com/#bytes
  [+] Starting local process '/home/input2/input2': pid 1283112
  [+] Opening connection to localhost on port 4444: Done
  [*] Switching to interactive mode
  Welcome to pwnable.kr
  Let's see if you know how to give input to program
  Just give me correct inputs then you will get the flag :)
  Stage 1 clear!
  Stage 2 clear!
  Stage 3 clear!
  Stage 4 clear!
  Stage 5 clear!
  Mommy_now_I_know_how_to_pa5s_inputs_in_Linux
  [*] Process '/home/input2/input2' stopped with exit code 0 (pid 1283112)
  [*] Got EOF while reading in interactive
```
- So the Flag is **Mommy_now_I_know_how_to_pa5s_inputs_in_Linux**
