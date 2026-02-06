# URL
https://training.olicyber.it/challenges#challenge-352

# Concept 
To get only the required and neccessary stuff and text from the website by filtering out the web result

# Method of Solve
- Go to the challenge interface and copy the target URL
- Now lets write a python script for solving the challenge and getting the flag
  ```
    import requests
    from bs4 import BeautifulSoup
    
    url = "http://web-13.challs.olicyber.it/"
    
    req = requests.get(url)
    
    page = BeautifulSoup(req.text, 'html.parser')
    
    spans = page.find_all('span')
    
    flag = "flag{"
    
    for span in spans:
        
        flag += span.text
        
    flag += "}"
    print(flag)
  ```
- What this script does s .. it takes the url and perform get request method on it
- Then it parses the html of the response after converting it into the text using the BeautifulSoap library functions
- then we tried ti find the span using the findall library from BeautifulSoap
- and lastly we operated a loop to print the findings as result
- The flag is **flag{donotrecommenddoingthisbyhand}**
