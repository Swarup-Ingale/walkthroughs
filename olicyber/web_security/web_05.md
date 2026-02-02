# URL
https://training.olicyber.it/challenges#challenge-344

# Concept
This Challenge helps us understand what are cookies and how they help in authentication mechanisms to give authorization to the particular users and also how they help in session management.
This Challenge also helps us understand how we can set cookies in a http request manually.

# Method of Solve
- Go to Challenge Interface and copy the Targer URL
- use curl in verbose mode using -v flag to Perform a GET request on the URL and get details about the website
- We will see that we get Bad request and Unauthorized due to cookie policy
  ```
    └─$ curl -X GET -v http://web-05.challs.olicyber.it/flag 
        Note: Unnecessary use of -X or --request, GET is already inferred.
        * Host web-05.challs.olicyber.it:80 was resolved.
        * IPv6: 64:ff9b::54b:dd30
        * IPv4: 5.75.221.48
        *   Trying [64:ff9b::54b:dd30]:80...
        * Established connection to web-05.challs.olicyber.it (64:ff9b::54b:dd30 port 80) from fd17:625c:f037:2:b99f:48b5:9f66:6ee9 port 37206 
        * using HTTP/1.x
        > GET /flag HTTP/1.1
        > Host: web-05.challs.olicyber.it
        > User-Agent: curl/8.18.0
        > Accept: */*
        > 
        * Request completely sent off
        < HTTP/1.1 401 Unauthorized
        < Content-Length: 33
        < Content-Type: text/plain; charset=utf-8
        < Date: Mon, 02 Feb 2026 11:06:42 GMT
        < Server: nginx/1.21.6
        < 
        * Connection #0 to host web-05.challs.olicyber.it:80 left intact
        Bad password cookie. Unauthorized
  ```
- Now run nc on the target URL to perform GET request and set cookies
  ```
    └─$ nc web-05.challs.olicyber.it 80  
        GET /flag HTTP/1.1
        Host: web-05.challs.olicyber.it
        Cookie: password=admin
        
        HTTP/1.1 200 OK
        Content-Length: 24
        Content-Type: text/plain; charset=utf-8
        Date: Mon, 02 Feb 2026 11:08:08 GMT
        Server: nginx/1.21.6
        
        flag{v3ry_7457y_c00ki35}
  ```
- And hence we get the Flag after setting Cookie Header for password=admin
- The Flag is **flag{v3ry_7457y_c00ki35}**
