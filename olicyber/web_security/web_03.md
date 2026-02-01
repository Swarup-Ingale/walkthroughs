# URL
https://training.olicyber.it/challenges#challenge-342

# Concept
To learn to set headers manually in the request (here GET and header X-Password)

# Method of Solve
- Go to Challenge interface and copy the link provided for the flag
- Open terminal and perfom curl on the URL
    ```
    └─$ curl -X GET -v http://web-03.challs.olicyber.it
        Note: Unnecessary use of -X or --request, GET is already inferred.
        * Host web-03.challs.olicyber.it:80 was resolved.
        * IPv6: 64:ff9b::54b:dd30
        * IPv4: 5.75.221.48
        *   Trying [64:ff9b::54b:dd30]:80...
        *   Trying 5.75.221.48:80...
        * Established connection to web-03.challs.olicyber.it (64:ff9b::54b:dd30 port 80) from fd17:625c:f037:2:b99f:48b5:9f66:6ee9 port 56254 
        * using HTTP/1.x
        > GET / HTTP/1.1
        > Host: web-03.challs.olicyber.it
        > User-Agent: curl/8.18.0
        > Accept: */*
        > 
        * Request completely sent off
        < HTTP/1.1 404 Not Found
        < Content-Length: 207
        < Content-Type: text/html; charset=utf-8
        < Date: Sun, 01 Feb 2026 07:11:17 GMT
        < Server: nginx/1.21.6
        < 
        <!doctype html>
        <html lang=en>
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
        * Connection #0 to host web-03.challs.olicyber.it:80 left intact
    ```
- Now as we can see we ran curl in verbose mode with -v flag to get all the details about the Host, HTTP Version, etc
- Then start netcat as nc
    ```
    └─$ nc web-03.challs.olicyber.it 80                  
        GET /flag HTTP/1.1
        Host: web-03.challs.olicyber.it:80
        X-Password: admin
        
        HTTP/1.1 200 OK
        Content-Length: 28
        Content-Type: text/plain; charset=utf-8
        Date: Sun, 01 Feb 2026 07:12:51 GMT
        Server: nginx/1.21.6
        
        flag{7ru57_m3_i_m_7h3_4dmin}
    ```
- As you can see we started nc on the provided url with the port 80
- Then we sent GET request for endpoint /flag with HTTP version 1.1
- we got Host from curl we ran above and we set X-Password as admin
- we get the flag
- The flag is **flag{7ru57_m3_i_m_7h3_4dmin}**
