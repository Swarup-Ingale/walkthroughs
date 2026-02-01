# URL
https://training.olicyber.it/challenges#challenge-341

# Concept
To learn to perform GET request by passing paramters through GET request 

# Method of Solve
- Go the Challenge interface
- go to terminal and start python and then import requests
    ```
    >> python
    >> import requests
    >> r = requests.get("http://web-02.challs.olicyber.it/server-records?id=flag")
    >> r.text
    >> print(r.text)

    ```
- we get the flag
- Here we passed **?id=flag** as paramter to our given url in our get request
- The Flag is **flag{wh47_i5_y0ur_qu3ry}**
