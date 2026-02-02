# URL
https://training.olicyber.it/challenges#challenge-348

# Concept
Now we are going to learn about how can we perform a POST request with specified or required Content-Type instead of good old application/x-www-form-urlencoded (here json)

# Method of Solve
- Go to the Challenge Interface and copy the targer URL
- Now we will perform a POST request using nc with specified Content-Type i.e. json
- This can be done using Content-Type header set to **application/json**
  ```
    └─$ nc  web-09.challs.olicyber.it 80
        POST /login HTTP/1.1
        Host: web-09.challs.olicyber.it
        Content-Type: application/json
        Content-Length: 39
        
        {"username":"admin","password":"admin"}
        HTTP/1.1 200 OK
        Content-Length: 47
        Content-Type: application/json
        Date: Mon, 02 Feb 2026 11:53:54 GMT
        Server: nginx/1.21.6
        
        {
          "token": "flag{w31c0m3_70_7h3_y34r_2000}"
        }
  ```
- Hence we ge the flag in the response body in a json format
- The flag is **flag{w31c0m3_70_7h3_y34r_2000}**
