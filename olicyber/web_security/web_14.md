# URL
https://training.olicyber.it/challenges#challenge-353

# Concept
To Look for the commented part of the sourcode of the HTML webpage as some juicy stuff might be hidden in there

# Method of Solve
- Go to the Challenge Interface and Copy the Target URL
- Now we can either visit the page and Look for the source code by doing **ctrl+shift+I** to open the dev tools
- OR we can just write a Python script to Print all the html contents of the target page
  ```
    import requests
    from bs4 import BeautifulSoup
    
    url = "http://web-14.challs.olicyber.it/"
    req = requests.get(url)
    page = BeautifulSoup(req.text, 'html.parser')
    
    print(page)
  ```
- The flag is **flag{50m3b0dy_f0rg07_70_d31373_7hi5}**
