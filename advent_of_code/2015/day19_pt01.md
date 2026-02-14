# URL
https://adventofcode.com/2015/day/19

# Description
Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:
```
H => HO
H => OH
O => HH
```
Given the replacements above and starting with HOH, the following molecules could be generated:
```
HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).
```
So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

# Method of Solve
- The challenge can be solved using the following code :
  ```
    def count_distinct_molecules(replacements, molecule):
        results = set()
    
        for src, dst in replacements:
            start = 0
            while True:
                idx = molecule.find(src, start)
                if idx == -1:
                    break
    
                new_molecule = (
                    molecule[:idx] +
                    dst +
                    molecule[idx + len(src):]
                )
                results.add(new_molecule)
    
                start = idx + 1
    
        return len(results)
    
    
    replacements = []
    molecule = ""
    
    with open("input_19_01") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "=>" in line:
                a, b = line.split(" => ")
                replacements.append((a, b))
            else:
                molecule = line
    
    print(count_distinct_molecules(replacements, molecule))
  ```
 # This Solves the part 01 of the Challenge.
