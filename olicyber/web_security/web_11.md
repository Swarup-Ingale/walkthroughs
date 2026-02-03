# URL
https://training.olicyber.it/challenges#challenge-350

# Concept
CSRF tokens are location- and method-specific — sending the right value in the wrong place is equivalent to sending no token at all.

# Method of Solve
- Go to the Challenge interface and copy the target URL
- get info about the URL and Server hosting it using nc
- Perform a POST request to the Server on the URL wiht the provided credentials
  ```
    └─$ nc web-11.challs.olicyber.it 80
        POST /login HTTP/1.1
        Host: web-11.challs.olicyber.it
        Content-Type: application/json
        Content-Length: 39
        
        {"username":"admin","password":"admin"}
        HTTP/1.1 200 OK
        Content-Length: 50
        Content-Type: application/json
        Date: Tue, 03 Feb 2026 13:53:14 GMT
        Server: nginx/1.21.6
        Set-Cookie: session=c4bbbb90-dd9e-4b7d-b568-e885c96dfc45; Path=/
        
        {
          "status": "ok",
          "csrf": "16d887d96b48c820"
        }
  ```
- Now as we can see we get an csrf-token and a cookie set to a value
- Now lets try to abuse the server by doing a GET request with the session cookie and csrf token
  ```
    GET /flag_piece?csrf=16d887d96b48c820 HTTP/1.1
        Host: web-11.challs.olicyber.it
        Cookie: session=c4bbbb90-dd9e-4b7d-b568-e885c96dfc45
        
        HTTP/1.1 400 Bad Request
        Content-Length: 58
        Content-Type: application/json
        Date: Tue, 03 Feb 2026 13:53:58 GMT
        Server: nginx/1.21.6
        
        {
          "error": "Bad Request",
          "message": "Missing index"
        }
  ```
  - Now as we can see the response body tells us about the missing parameter index, so now lets apply the index from 0,1,2,..... Untill we get the entire flag
    ```
      └─$ nc web-11.challs.olicyber.it 80
          POST /login HTTP/1.1
          Host: web-11.challs.olicyber.it
          Content-Type: application/json
          Content-Length: 39
          
          {"username":"admin","password":"admin"}
          HTTP/1.1 200 OK
          Content-Length: 50
          Content-Type: application/json
          Date: Tue, 03 Feb 2026 13:45:48 GMT
          Server: nginx/1.21.6
          Set-Cookie: session=f7314daf-e058-4ad6-9185-4ed81577c9ed; Path=/
          
          {
            "status": "ok",
            "csrf": "0971ea4a87ce6eaf"
          }
          GET /flag_piece?csrf=0971ea4a87ce6eaf&index=0 HTTP/1.1
          Host: web-11.challs.olicyber.it
          Cookie: session=f7314daf-e058-4ad6-9185-4ed81577c9ed
          
          HTTP/1.1 200 OK
          Content-Length: 62
          Content-Type: application/json
          Date: Tue, 03 Feb 2026 13:46:46 GMT
          Server: nginx/1.21.6
          
          {
            "flag_piece": "flag{v3ry_",
            "csrf": "5d8daa0b645740a0"
          }
    ```
- Now we will perform similar pattern of requests with different indexes and csrf tokens for every index until we get the entire flag data
  ```
    └─$ nc web-11.challs.olicyber.it 80
        POST /login HTTP/1.1
        Host: web-11.challs.olicyber.it
        Content-Type: application/json
        Content-Length: 39
        
        {"username":"admin","password":"admin"}
        HTTP/1.1 200 OK
        Content-Length: 50
        Content-Type: application/json
        Date: Tue, 03 Feb 2026 13:47:58 GMT
        Server: nginx/1.21.6
        Set-Cookie: session=6447d8bb-023d-4be5-b12a-39f7af68fcc9; Path=/
        
        {
          "status": "ok",
          "csrf": "237b727cf7872726"
        }
        GET /flag_piece?csrf=237b727cf7872726&index=1 HTTP/1.1
        Host: web-11.challs.olicyber.it
        Cookie: session=6447d8bb-023d-4be5-b12a-39f7af68fcc9
        
        HTTP/1.1 200 OK
        Content-Length: 62
        Content-Type: application/json
        Date: Tue, 03 Feb 2026 13:48:44 GMT
        Server: nginx/1.21.6
        
        {
          "flag_piece": "53ri0u5_53",
          "csrf": "62828caca98d9765"
        }
  ```
- Finally we get entire flag after few rounds
- The Flag is **flag{v3ry_53ri0u5_53ri35_0f_r3qu3575}**
