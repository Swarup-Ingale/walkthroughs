# URL
https://training.olicyber.it/challenges#challenge-345

# Concept
How Cookies are generated and how they help in **Session Management**. Also How can we manipulate user cookies to get the handle of session

# Method of Solve
- Go to the Challenge interface and copy the Target URL which generates a cookie or sets a coookie for the main URL session
- use curl in verbose mode using -v flag to send a GET request to the token generating URL :
  ```
    └─$ curl -X GET -v http://web-06.challs.olicyber.it/token
        Note: Unnecessary use of -X or --request, GET is already inferred.
        * Host web-06.challs.olicyber.it:80 was resolved.
        * IPv6: 64:ff9b::54b:dd30
        * IPv4: 5.75.221.48
        *   Trying [64:ff9b::54b:dd30]:80...
        * Established connection to web-06.challs.olicyber.it (64:ff9b::54b:dd30 port 80) from fd17:625c:f037:2:b99f:48b5:9f66:6ee9 port 50744 
        * using HTTP/1.x
        > GET /token HTTP/1.1
        > Host: web-06.challs.olicyber.it
        > User-Agent: curl/8.18.0
        > Accept: */*
        > 
        * Request completely sent off
        < HTTP/1.1 204 No Content
        < Content-Type: text/html; charset=utf-8
        < Date: Mon, 02 Feb 2026 11:16:25 GMT
        < Server: nginx/1.21.6
        < Set-Cookie: token=e94a3eb9-594c-4fd5-be05-c5e648c1c71c; Path=/
        < 
        * Connection #0 to host web-06.challs.olicyber.it:80 left intact
  ```
- Now as we can see, we got a Cookie set using Set-Cookie header for token = .....
- Now lets use this cookie to open the session on target URL and get the flag
  ```
    └─$ nc web-06.challs.olicyber.it 80
        GET /flag HTTP/1.1
        Host: web-06.challs.olicyber.it
        Cookie: token=e94a3eb9-594c-4fd5-be05-c5e648c1c71c
        
        HTTP/1.1 200 OK
        Content-Length: 22
        Content-Type: text/plain; charset=utf-8
        Date: Mon, 02 Feb 2026 11:18:06 GMT
        Server: nginx/1.21.6
        
        flag{7w0_574g3_4cc3s5}
  ```
- We get the flag and the flag is **flag{7w0_574g3_4cc3s5}**    
