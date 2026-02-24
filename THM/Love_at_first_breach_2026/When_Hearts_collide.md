# URL
https://tryhackme.com/room/lafb2026e1

# Concept
To Learn about nginx server vulnerability of RCE and File Upload Vulnerability and about hash collision (MD5)

# Method of Solve
- Start the attack box or connect using openvpn
- Start Burpsuite and look for all the endpoints or explore all the endpoints and look for all the Contents and requests type in the endpoints
- Read the description and proceed accordingly
- Use Docker to access a tool which causes Creation of two files with idetical hash to perform hash collision
  ```
    ┌──(kali㉿kali)-[~/Downloads/fastcoll]
    └─$ docker pull brimstone/fastcoll
  ```
- After that lets create the hashed identical files
  ```
    - ┌──(kali㉿kali)-[~/Downloads/fastcoll]
      └─$ docker run --rm -v $PWD:/work -w /work brimstone/fastcoll \                                                       
      >  --prefixfile dog.jpg -o collision1.jpg collision2.jpg
  ```
- Check if the files exists
  ```                                                                                                                                      
    ┌──(kali㉿kali)-[~/Downloads/fastcoll]
    └─$ ls
        collision2.jpg  dog.jpg  collision1.jpg
  ```
- Where **dog.jpg** is the original file and **collision1.jpg** and **collision2.jpg** are the files with identical md5 hash
- Now check the hash of both the files
  ```
    ┌──(kali㉿kali)-[~/Downloads/fastcoll]
    └─$ md5sum collision1.jpg collision2.jpg 
    79403cf512a1d747aedb7ec93f13fa8b  collision1.jpg
    79403cf512a1d747aedb7ec93f13fa8b  collision2.jpg
  ```
- Now since the hashes match lets upload them both to the website
- The website Checks the hashes and matches them and gives the flag

## This Concludes the EP 01 of the Path.
