# URL
https://adventofcode.com/2018/day/19#part2

# Description
A new background process immediately spins up in its place. It appears identical, but on closer inspection, you notice that this time, register 0 started with the value 1.

What value is left in register 0 when this new background process halts?

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python version is as follows:
```
n = 10551373

ans = 0

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        ans += i
        if i != n // i:
            ans += n // i

print(ans)
```
- The Javascript version is as follows:
```
const n = 10551373;

let ans = 0;

for (let i = 1; i * i <= n; i++) {
    if (n % i === 0) {
        ans += i;
        if (i !== n / i)
            ans += n / i;
    }
}

console.log(ans);
```

# This Concludes Day 19 of The Advent of Code.
