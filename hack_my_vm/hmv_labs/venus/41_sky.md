# Target User
sarah  -pass: LWOHeRgmIxg7fuS

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat mission.txt
- Use curl command to get the details about the URL in verbose mode using the -v flag
  ```
    sky@venus:~$ curl -v "http://localhost/key.php"
    *   Trying 127.0.0.1:80...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > GET /key.php HTTP/1.1
    > Host: localhost
    > User-Agent: curl/7.88.1
    > Accept: */*
    > 
    < HTTP/1.1 200 OK
    < Server: nginx/1.22.1
    < Date: Mon, 02 Mar 2026 14:14:20 GMT
    < Content-Type: text/html; charset=UTF-8
    < Transfer-Encoding: chunked
    < Connection: keep-alive
    < 
    
    Key header is true?
    * Connection #0 to host localhost left intact
  ```
- The response reveals that the Key Header should be set to value true so lets set that using the -H flag
  ```
    sky@venus:~$ curl -v -H "Key: true" "http://localhost/key.php"
    *   Trying 127.0.0.1:80...
    * Connected to localhost (127.0.0.1) port 80 (#0)
    > GET /key.php HTTP/1.1
    > Host: localhost
    > User-Agent: curl/7.88.1
    > Accept: */*
    > Key: true
    > 
    < HTTP/1.1 200 OK
    < Server: nginx/1.22.1
    < Date: Mon, 02 Mar 2026 14:14:47 GMT
    < Content-Type: text/html; charset=UTF-8
    < Transfer-Encoding: chunked
    < Connection: keep-alive
    < 
    
    * Connection #0 to host localhost left intact
    LWOHeRgmIxg7fuS
  ```
- The Password is revealed in the response
- The password is **LWOHeRgmIxg7fuS**

# Commands Used
- ls -la
- cat
- curl
