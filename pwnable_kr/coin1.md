# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh coin1@pwnable.kr -p2222 (pw: guest)

# Source Code
- No source code for this challenge
- Just start nc at 0 and port 9007 and play the game
  ```
    nc 0 9007
  ```

# Concept
To Understand how binary search works and how can we implement it in real world scenarios

# Method of Solve
- Go to the challenge URL and connect using the SSH Credentials
- cat the readme file to understand what we have to do in the challenge.
- The readme says to connect to listen on 0 and port 9007 using nc.
- Now we have to play a game for searching the coins in given chances and no of coins.
- For this we will use the **BINARY SEARCH** where, the input is divided into halves everytime for searching and it is searched from the central element of the divided input.
- The Code for performing binary search is as follows:
  ```
    from pwn import *

    # For SSHing in, and then running locally
    # s = ssh(host="pwnable.kr", user="fd", port=2222, password="guest")
    # conn = s.remote('localhost', 9007)
    
    # For running remotely
    # conn = remote('pwnable.kr', 9007)
    
    # For running locally on pwnable.kr
    conn = remote('localhost', 9007)
    
    conn.recvuntil('Ready? starting in 3 sec')
    conn.recvline()
    conn.recvline()
    
    for _ in range(100):
            
            line = conn.recvline().decode('utf-8').strip().split(' ') # [u'N=317', u'C=9']
            # print line
            n = int(line[0].split('=')[1])  # 317
            c = int(line[1].split('=')[1])  # 9
    
            start = 0
            end = n - 1
    
            for _ in range(c):
    
                    mid = int((start + end)/2) # cast to ensure only whole numbers
    
                    # print('start: '+str(start))
                    # print('mid: '+str(mid))
                    # print('end: '+str(end))
    
                    guess = ' '.join(str(i) for i in range(start, mid + 1))
                    # print guess
                    conn.sendline(guess)
                    weight = int(conn.recvline())
                    # print weight
                    
                    if weight % 10 == 0: # if divisible by 10, then no counterfeit in list
                            start = mid + 1
                    else: # counterfeit in list
                            end = mid
    
            conn.sendline(str(start)) # send final guess
    
            print(conn.recvline())  # Correct! (n)
    
    print(conn.recvline()) # Congrats! get your flag
    print(conn.recvline()) # {actual flag}
    
    conn.close()
  ```
- Here first we form a connection and connect to the nc 0 9007.
- then we start our search after taking the N (No. of coins) and C (Chances) as input.
- The Binary search divides the input of N into two equal halves for each iteration and searches until the desired coins are not found.
- Once found the flag is printed.
- The Flag is **b1naRy_S34rch1Ng_1s_3asy_p3asy**
