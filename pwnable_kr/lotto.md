# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh lotto@pwnable.kr -p2222 (pw:guest)

# Source Code

  ```
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <fcntl.h>
    
    unsigned char submit[6];
    
    void play(){
    	
    	int i;
    	printf("Submit your 6 lotto bytes : ");
    	fflush(stdout);
    
    	int r;
    	r = read(0, submit, 6);
    
    	printf("Lotto Start!\n");
    	//sleep(1);
    
    	// generate lotto numbers
    	int fd = open("/dev/urandom", O_RDONLY);
    	if(fd==-1){
    		printf("error. tell admin\n");
    		exit(-1);
    	}
    	unsigned char lotto[6];
    	if(read(fd, lotto, 6) != 6){
    		printf("error2. tell admin\n");
    		exit(-1);
    	}
    	for(i=0; i<6; i++){
    		lotto[i] = (lotto[i] % 45) + 1;		// 1 ~ 45
    	}
    	close(fd);
    	
    	// calculate lotto score
    	int match = 0, j = 0;
    	for(i=0; i<6; i++){
    		for(j=0; j<6; j++){
    			if(lotto[i] == submit[j]){
    				match++;
    			}
    		}
    	}
    
    	// win!
    	if(match == 6){
    		setregid(getegid(), getegid());
    		system("/bin/cat flag");
    	}
    	else{
    		printf("bad luck...\n");
    	}
    
    }
    
    void help(){
    	printf("- nLotto Rule -\n");
    	printf("nlotto is consisted with 6 random natural numbers less than 46\n");
    	printf("your goal is to match lotto numbers as many as you can\n");
    	printf("if you win lottery for *1st place*, you will get reward\n");
    	printf("for more details, follow the link below\n");
    	printf("http://www.nlotto.co.kr/counsel.do?method=playerGuide#buying_guide01\n\n");
    	printf("mathematical chance to win this game is known to be 1/8145060.\n");
    }
    
    int main(int argc, char* argv[]){
    
    	// menu
    	unsigned int menu;
    
    	while(1){
    
    		printf("- Select Menu -\n");
    		printf("1. Play Lotto\n");
    		printf("2. Help\n");
    		printf("3. Exit\n");
    
    		scanf("%d", &menu);
    
    		switch(menu){
    			case 1:
    				play();
    				break;
    			case 2:
    				help();
    				break;
    			case 3:
    				printf("bye\n");
    				return 0;
    			default:
    				printf("invalid menu\n");
    				break;
    		}
    	}
    	return 0;
    }
  ```

# Concept 
This Challenge contains a logical vulnerability in its matching algorithm. Due to improper validation and lack of duplicate handling in nested comparison loops, the match counter can be manipulated by submitting repeated bytes. This reduces the effective complexity of the intended lottery logic and allows exploitation through repeated attempts rather than brute-forcing a full 6-number combination.

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and inspect the lotto.c file
- As we can see... there exists a logic flaw in the source code in this section :
  ```
    for(i=0; i<6; i++){
        for(j=0; j<6; j++){
            if(lotto[i] == submit[j]){
                match++;
            }
        }
    }
  ```
- as we can see the program in this section is failing to check the **uniqueness** of the generated random number and submitted random number
- Hence if we input similar value of '$' 6 times for 6 inputs... The program will store it and use it for comparission
- Due to this and no uniqueness check we get flag after 6 same inputs
  ```
    lotto@ubuntu:~$ ./lotto 
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    bad luck...
    - Select Menu -
    1. Play Lotto
    2. Help
    3. Exit
    1
    Submit your 6 lotto bytes : $$$$$$
    Lotto Start!
    Sorry_mom_1_Forgot_to_check_duplicates
  ```
- Hence we successfully get the flag.
- The Flag is **Sorry_mom_1_Forgot_to_check_duplicates**
