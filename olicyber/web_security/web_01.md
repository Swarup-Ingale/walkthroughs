# URL
https://training.olicyber.it/challenges#challenge-340

# Concept 
To understand how web actually work and to perform a GET request on the website 

# Method of Solve
- Download the challenge.py file from the Challenge interface
- Open the file and try to understand it
- Now start python in terminal and import requests
  ```
  python
  import requests
  r = requests.get("http://web-01.challs.olicyber.it/")
  r.text
  print(r.text)

  ```
- we will get the flag
- The flag is **flag{g3t7ing_4l0ng}**
