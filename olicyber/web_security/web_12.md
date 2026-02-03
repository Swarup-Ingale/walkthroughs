# URL
https://training.olicyber.it/challenges#challenge-351

# Concept
Understanding what is HTML and how it is used in Web Security as well as exploitation by Extracting Simple Content from a Web Page.

# Method of Solve
- Go to the Challenge Interface and copy the target URL
- perform a GET request using curl command in verbose mode using -v flag
- It dumps all the raw HTML data of the website when run in verbose mode
- Now look for the flag in the paragraphs
- The flag is in the 2nd paragrapgh
  ```
    └─$ curl -X GET -v http://web-12.challs.olicyber.it/     
        Note: Unnecessary use of -X or --request, GET is already inferred.
        * Host web-12.challs.olicyber.it:80 was resolved.
        * IPv6: 64:ff9b::54b:dd30
        * IPv4: 5.75.221.48
        *   Trying [64:ff9b::54b:dd30]:80...
        *   Trying 5.75.221.48:80...
        * Established connection to web-12.challs.olicyber.it (64:ff9b::54b:dd30 port 80) from fd17:625c:f037:2:b99f:48b5:9f66:6ee9 port 45042 
        * using HTTP/1.x
        > GET / HTTP/1.1
        > Host: web-12.challs.olicyber.it
        > User-Agent: curl/8.18.0
        > Accept: */*
        > 
        * Request completely sent off
        < HTTP/1.1 200 OK
        < Content-Length: 2440
        < Content-Type: text/html; charset=utf-8
        < Date: Tue, 03 Feb 2026 14:04:16 GMT
        < Server: nginx/1.21.6
        < 
        <!doctype HTML>
        
        <html>
          <head>
            <title>Daily lipsum</title>
            <style>
              body {
                min-height: 100vh;
                max-width: 40em;
                margin: 0 auto;
                padding: 2em;
                align: center;
                text-align: justify;
                font-family: Sans-Serif;
              }
            </style>
          </head>
          <body>
            <h1>Daily lipsum</h1>
            <p>
              .
              .
              .
            </p>
            <p>
              <pre>flag{7h3_14ngu4g3_0f_7h3_w3b}</pre>
            </p>
            <p>
              .
              .
              .
            </p>
            <p>
              .
              .
              .
            </p>
            <p>
              .
              .
              .
            </p>
          </body>
        * Connection #0 to host web-12.challs.olicyber.it:80 left intact
        </html>
- The Flag is **flag{7h3_14ngu4g3_0f_7h3_w3b}**
