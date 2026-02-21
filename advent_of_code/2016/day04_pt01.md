# URL
https://adventofcode.com/2016/day/4

# Description
Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:
```
aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
```
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

# Method of Solve
- The part 01 of this chaallenge can be solved using the following code:
  ```
    total = 0
    
    with open("input_04", "r") as file:
        lines = file.read().splitlines()
    
    for line in lines:
        # Split name from sector/checksum
        name_part, rest = line.rsplit("-", 1)
    
        # Extract sector ID and checksum
        sector_id = int(rest.split("[")[0])
        checksum = rest.split("[")[1][:-1]
    
        # Count letter frequencies (ignore dashes)
        counts = {}
        for ch in name_part:
            if ch != "-":
                counts[ch] = counts.get(ch, 0) + 1
    
        # Sort letters by frequency desc, then alphabetically
        sorted_letters = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
        # Build calculated checksum
        calculated_checksum = "".join(letter for letter, _ in sorted_letters[:5])
    
        # Check if room is real
        if calculated_checksum == checksum:
            total += sector_id
    
    print("Sum of sector IDs of real rooms:", total)
  ```
- This Solves the part 01 of the challenge.
