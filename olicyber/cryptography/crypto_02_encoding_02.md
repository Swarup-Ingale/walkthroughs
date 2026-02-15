# URL
https://training.olicyber.it/challenges#challenge-327

# Concept
To understand the HEX encoding and how to identify and decode it

# Method of Solve
- Go to the Challenge URL and copy the hex encoded flag value
- Visit the cyberchef and decode it using FROM HEX or else use the python script
  ```
    hex_string = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"

    decoded = bytes.fromhex(hex_string).decode("ascii")
    print(decoded)
  ```
- The flag is **flag{h3x4decimal_c4n_b3_ABADBABE}**
