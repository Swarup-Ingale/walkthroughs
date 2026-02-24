# URL
https://tryhackme.com/room/lafb2026e5

# Concept 
Manipulating JWT Tokens for manipualtion of contents and cookies 

# Method of Solve
- Start the attack box or connect using openvpn
- Start Burpsuite and look for all the endpoints or explore all the endpoints and look for all the Contents and requests type in the endpoints
- Read the description and proceed accordingly
- Then lets look for any suspicious endpoint or content-type or cookie header in the requests and responses in burp
- As we can see the website uses jwt encoding in cookies so now lets decode it
- Lets use jwt.io and Jwt decoder to decode and frame a admin user cookie with credits more than 2000
- Then paste the cookie in dev tools storage cookies container
- Reload the page and get the flag after purchasing the flag item

## This Concludes the EP 05 of the PATH.
