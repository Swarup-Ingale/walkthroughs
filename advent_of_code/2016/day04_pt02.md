# URL
https://adventofcode.com/2016/day/4#part2

# Description
With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

# Method of Solve
- The part 02 of this challenge can be solved using the following code:
  ```
    with open("input_04", "r") as file:
        lines = file.read().splitlines()
    
    for line in lines:
        # Split encrypted name and rest
        name_part, rest = line.rsplit("-", 1)
    
        sector_id = int(rest.split("[")[0])
        checksum = rest.split("[")[1][:-1]
    
        # PART 1 CHECK (is real room?)
        counts = {}
        for ch in name_part:
            if ch != "-":
                counts[ch] = counts.get(ch, 0) + 1
    
        sorted_letters = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        calculated_checksum = "".join(letter for letter, _ in sorted_letters[:5])
    
        if calculated_checksum != checksum:
            continue  # skip decoy rooms
    
        # PART 2 DECRYPTION
        decrypted = ""
    
        for ch in name_part:
            if ch == "-":
                decrypted += " "
            else:
                shifted = (ord(ch) - ord("a") + sector_id) % 26
                decrypted += chr(ord("a") + shifted)
    
        # Check for target room
        if "northpole object storage" in decrypted:
            print("Sector ID:", sector_id)
            print("Decrypted name:", decrypted)
  ```

# This Concludes the Day 04 of The Advent of Code.
