# URL
https://training.olicyber.it/challenges#challenge-354

# Concept
To Find all the pages and scripts and css files to get the information ... basically snooping 

# Method of Solve
- Go to the challenge Interface and copy the target URL
- Now we can solve this challenge using two methods ... 1st is directly accessing the webpage and snooping manually which is hectic
- OR 2nd method is using python scripts to automate this process and get the data faster
  ```
    import requests
    from bs4 import BeautifulSoup
    
    url = "http://web-15.challs.olicyber.it/"
    
    req = requests.get(url)
    
    page = BeautifulSoup(req.text, 'html.parser')
    
    links = page.find_all('link')
    scripts = page.find_all('script')
    
    for link in links:
        page = requests.get(f"{url}{link.attrs['href']}").text
        if "flag" in page:
            print(page)
            break
        
    for script in scripts:
        page = requests.get(f"{url}{script.attrs['src']}").text
        if "flag" in page:
            print(page)
            break
  ```
- The flag is **flag{5n00ping_4r0und}**
