# Target User
veronica  -pass: QTOel6BodTx2cwX

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat mission.txt
- Then use curl -A flag to spoof the User Agent Header in the request
  ```
    kira@venus:~$ curl -A "PARADISE" -v http://localhost/waiting.php
    *   Trying 127.0.0.1:80...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > GET /waiting.php HTTP/1.1
    > Host: localhost
    > User-Agent: PARADISE
    > Accept: */*
    > 
    < HTTP/1.1 200 OK
    < Server: nginx/1.22.1
    < Date: Sat, 21 Feb 2026 16:56:32 GMT
    < Content-Type: text/html; charset=UTF-8
    < Transfer-Encoding: chunked
    < Connection: keep-alive
    < 
    
    QTOel6BodTx2cwX 
    * Connection #0 to host localhost left intact
  ```
- This will print the password.

# Commands Used 
- ls -la
- cat
- curl
