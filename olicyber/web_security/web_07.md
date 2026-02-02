# URL
https://training.olicyber.it/challenges#challenge-346

# Concept
How to get only headers of the URL and study them if we are not authorized to access the Website

# Method of Solve
- Go to the Challenge interface and copy the target URL
- use curl with -I flag to get only headers of the URL without actually sending and request
  ```
    └─$ curl -I http://web-07.challs.olicyber.it/ 
        HTTP/1.1 401 Unauthorized
        Content-Length: 12
        Content-Type: text/plain; charset=utf-8
        Date: Mon, 02 Feb 2026 11:27:14 GMT
        Server: nginx/1.21.6
        X-Flag: flag{r0gu3_m374d474}
  ```
- And we got the flag in the headers of the response
- The flag is **flag{r0gu3_m374d474}**
