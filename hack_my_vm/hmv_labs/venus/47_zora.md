# Target User
belen  -pass: 2jA0E8bQ4WrGwWZ

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- inspect all the hosts in /etc/hosts file
- it states a venus host
  ```
    zora@venus:~$ cat /etc/hosts
    127.0.0.1	localhost
    ::1	localhost ip6-localhost ip6-loopback
    fe00::	ip6-localnet
    ff00::	ip6-mcastprefix
    ff02::1	ip6-allnodes
    ff02::2	ip6-allrouters
    172.66.0.10	venus
  ```
- Now Lets connect the venus.hmv using curl
  ```
    zora@venus:~$ curl -v venus.hmv
    *   Trying 172.66.0.10:80...
    * Connected to venus.hmv (172.66.0.10) port 80 (#0)
    > GET / HTTP/1.1
    > Host: venus.hmv
    > User-Agent: curl/7.88.1
    > Accept: */*
    > 
    < HTTP/1.1 200 OK
    < Server: nginx/1.22.1
    < Date: Mon, 02 Mar 2026 15:16:58 GMT
    < Content-Type: text/html
    < Content-Length: 16
    < Last-Modified: Fri, 05 Apr 2024 06:28:46 GMT
    < Connection: keep-alive
    < ETag: "660f9a1e-10"
    < Accept-Ranges: bytes
    < 
    2jA0E8bQ4WrGwWZ
    * Connection #0 to host venus.hmv left intact
  ```
- The Password is **2jA0E8bQ4WrGwWZ**

# Commands Used
- ls -la
- cat
- curl
