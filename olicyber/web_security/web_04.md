# URL
https://training.olicyber.it/challenges#challenge-343

# Concept
This challenge helps us understand the structure of http request-response header and how can we manipulate it and what happens if we manipulate it according to our will (here **Accept** Header)

# Method of Solve
- Go to the challenge interface and copy the target url
- use curl to get the response of GET request to the URL in verbose mode using -v flag:
  ```
    ─$ curl -X GET -v http://web-04.challs.olicyber.it/users
      Note: Unnecessary use of -X or --request, GET is already inferred.
      * Host web-04.challs.olicyber.it:80 was resolved.
      * IPv6: 64:ff9b::54b:dd30
      * IPv4: 5.75.221.48
      *   Trying [64:ff9b::54b:dd30]:80...
      *   Trying 5.75.221.48:80...
      * Established connection to web-04.challs.olicyber.it (64:ff9b::54b:dd30 port 80) from fd17:625c:f037:2:b99f:48b5:9f66:6ee9 port 60520 
      * using HTTP/1.x
      > GET /users HTTP/1.1
      > Host: web-04.challs.olicyber.it
      > User-Agent: curl/8.18.0
      > Accept: */*
      > 
      * Request completely sent off
      < HTTP/1.1 200 OK
      < Content-Length: 461
      < Content-Type: application/json
      < Date: Mon, 02 Feb 2026 10:57:37 GMT
      < Server: nginx/1.21.6
      < 
      {
        "users": [
          {
            "name": "admin",
            "role": "admin",
            "registration_date": "2018-06-18T15:34:55Z"
          },
          {
            "name": "fruitfly",
            "role": "user",
            "registration_date": "2019-08-12T12:04:32Z"
          },
          {
            "name": "jim87",
            "role": "user",
            "registration_date": "2022-01-13T20:09:43Z"
          },
          {
            "name": "anonymous05",
            "role": "user",
            "registration_date": "2022-03-09T16:01:07Z"
          }
        ]
      * Connection #0 to host web-04.challs.olicyber.it:80 left intact
      }
  ```
- Now we know the Host, and Accept Header
- Now lets set the Host header to the Host we got and Accept header to the required format i.e. application/xml
  ```
    ─$ nc web-04.challs.olicyber.it 80
      GET /users HTTP/1.1
      Host: web-04.challs.olicyber.it
      Accept: application/xml
      
      HTTP/1.1 200 OK
      Content-Length: 635
      Content-Type: application/xml; charset=utf-8
      Date: Mon, 02 Feb 2026 10:58:57 GMT
      Server: nginx/1.21.6
      
      <?xml version="1.0"?>
      
      <users>
        <user comment="flag{54m3_7hing_diff3r3n7_7hing}">
          <name>admin</name>
          <role>admin</role>
          <registration_date>2018-06-18T15:34:55Z</registration_date>
        </user>
        <user>
          <name>fruitfly</name>
          <role>user</role>
          <registration_date>2019-08-12T12:04:32Z</registration_date>
        </user>
        <user>
          <name>jim87</name>
          <role>user</role>
          <registration_date>2022-01-13T20:09:43Z</registration_date>
        </user>
        <user comment="Suspicious activity">
          <name>anonymous05</name>
          <role>user</role>
          <registration_date>2022-03-09T16:01:07Z</registration_date>
        </user>
      </users>
  ```
- Look for the flag in the response
- The flag is **flag{54m3_7hing_diff3r3n7_7hing}**
