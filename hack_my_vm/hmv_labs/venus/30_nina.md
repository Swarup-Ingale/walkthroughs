# Target User
kira   -pass: tPlqxSKuT4eP3yr

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat to read the mission.txt
- use curl with PUT method to put the method.php to get the flag
  ```
    nina@venus:~$ curl -X PUT -v http://localhost/method.php
    *   Trying 127.0.0.1:80...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > PUT /method.php HTTP/1.1
    > Host: localhost
    > User-Agent: curl/7.88.1
    > Accept: */*
    > 
    < HTTP/1.1 200 OK
    < Server: nginx/1.22.1
    < Date: Fri, 20 Feb 2026 16:51:33 GMT
    < Content-Type: text/html; charset=UTF-8
    < Transfer-Encoding: chunked
    < Connection: keep-alive
    < 
    
    tPlqxSKuT4eP3yr 
    * Connection #0 to host localhost left intact
  ```
- We get the password

# Commands Used
- ls -la
- cat
- curl 
