# URL
https://adventofcode.com/2018/day/4#part2

# Description
Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)

# Method of Solve
- The Part 02 of this challenge can be solved using the following code:
- The Python Version of solution is :
```
import re
from collections import defaultdict

with open("input_04") as f:
    logs = sorted(line.strip() for line in f)

minute_count = defaultdict(
    lambda: [0] * 60
)

guard = None
sleep_start = None

for log in logs:

    minute = int(log[15:17])

    if "Guard" in log:
        guard = int(
            re.search(
                r"#(\d+)",
                log
            ).group(1)
        )

    elif "falls asleep" in log:
        sleep_start = minute

    else:
        for m in range(
            sleep_start,
            minute
        ):
            minute_count[guard][m] += 1

best_guard = None
best_minute = None
best_count = 0

for guard in minute_count:

    for minute in range(60):

        if (
            minute_count[guard][minute]
            > best_count
        ):
            best_count = (
                minute_count[guard][minute]
            )

            best_guard = guard
            best_minute = minute

print(best_guard * best_minute)
```
- The Javascript version of the solution is :
```
const fs = require('fs');

const logs = fs
    .readFileSync('input_04', 'utf8')
    .trim()
    .split('\n')
    .sort();

const minuteCount = {};

let guard = null;
let sleepStart = null;

for (const log of logs) {

    const minute = Number(
        log.substring(15, 17)
    );

    if (log.includes('Guard')) {

        guard = Number(
            log.match(/#(\d+)/)[1]
        );

        if (!minuteCount[guard]) {
            minuteCount[guard] =
                Array(60).fill(0);
        }

    } else if (
        log.includes('falls asleep')
    ) {

        sleepStart = minute;

    } else {

        for (
            let m = sleepStart;
            m < minute;
            m++
        ) {
            minuteCount[guard][m]++;
        }
    }
}

let bestGuard = null;
let bestMinute = null;
let bestCount = 0;

for (const guard in minuteCount) {

    for (let m = 0; m < 60; m++) {

        if (
            minuteCount[guard][m]
            > bestCount
        ) {
            bestCount =
                minuteCount[guard][m];

            bestGuard =
                Number(guard);

            bestMinute = m;
        }
    }
}

console.log(
    bestGuard * bestMinute
);
```

# This Concludes The Dayv 04 of The Advent of Code.
