# URL
https://tryhackme.com/room/lafb2026e2

# Concept 
Path Traversal and File Inclusion Vulnerability

# Method of Solve
- Start the attack box or connect using openvpn
- Start Burpsuite and look for all the endpoints or explore all the endpoints and look for all the Contents and requests type in the endpoints
- Read the description and proceed accordingly
- We will see the path traversal vulnerability as we upload the letters the letter count increases by 1
  ```
    GET /letter/4 HTTP/1.1
    GET /letter/3 HTTP/1.1
  ```
- Now as we can see there were already 2 letters in the archive so lets try accessing them
  ```
    GET /letter/2 HTTP/1.1
  ```
- We get some phrases which are good to hear
  ```
    GET /letter/1 HTTP/1.1
  ```
- We get the flag here.

# This Concludes the EP 02 of the PATH.
