# URL
https://training.olicyber.it/challenges#challenge-347

# Concept
How can we perform FORM or Post requests to any website manually and how it afects the Website

# Method of Solve
- Go to the Challenge Interface and Copy the Target URL
- use nc to connect to the URL and send Post request to the website
- For this POST is used as request method and in Headers Content-Type and Content-Lenght is used
- For Post requests Content-Type **application/x-www-form-urlencoded** is used and since username=admin&password=admin is 29 bytes or 29b characters long the Content-Lenght is **29**
  ```
    └─$ nc  web-08.challs.olicyber.it 80
        POST /login HTTP/1.1
        Host:  web-08.challs.olicyber.it 
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 29
        
        username=admin&password=admin
        HTTP/1.1 200 OK
        Content-Length: 30
        Content-Type: text/plain; charset=utf-8
        Date: Mon, 02 Feb 2026 11:40:51 GMT
        Server: nginx/1.21.6
        
        flag{53nding_d474_7h3_01d_w4y}
  ```
- And We get the flag in response body
- The flag is **flag{53nding_d474_7h3_01d_w4y}**
