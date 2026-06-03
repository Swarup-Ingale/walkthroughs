# URL
https://adventofcode.com/2018/day/4

# Description
You've sneaked into another supply closet - this time, it's across from the prototype suit manufacturing lab. You need to sneak inside and fix the issues with the suit, but there's a guard stationed outside the lab, so this is as close as you can safely get.

As you search the closet for anything that might help, you discover that you're not the first person to want to sneak in. Covering the walls, someone has spent an hour starting every midnight for the past few months secretly observing this guard post! They've been writing down the ID of the one guard on duty that night - the Elves seem to have decided that one guard was enough for the overnight shift - as well as when they fall asleep or wake up while at their post (your puzzle input).

For example, consider the following records, which have already been organized into chronological order:
```
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
```
Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:
```
Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
```
The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
- The Python Version is :
```
import re
from collections import defaultdict

with open("input_04") as f:
    logs = sorted(line.strip() for line in f)

sleep_minutes = defaultdict(int)
minute_count = defaultdict(lambda: [0] * 60)

guard = None
sleep_start = None

for log in logs:

    minute = int(log[15:17])

    if "Guard" in log:
        guard = int(re.search(r"#(\d+)", log).group(1))

    elif "falls asleep" in log:
        sleep_start = minute

    elif "wakes up" in log:

        sleep_minutes[guard] += minute - sleep_start

        for m in range(sleep_start, minute):
            minute_count[guard][m] += 1

sleepiest_guard = max(
    sleep_minutes,
    key=sleep_minutes.get
)

best_minute = minute_count[sleepiest_guard].index(
    max(minute_count[sleepiest_guard])
)

print(sleepiest_guard * best_minute)
```
- The Javascript version is :
```
const fs = require('fs');

const logs = fs
    .readFileSync('input_04', 'utf8')
    .trim()
    .split('\n')
    .sort();

const sleepMinutes = {};
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

        if (!sleepMinutes[guard]) {
            sleepMinutes[guard] = 0;
        }

    } else if (
        log.includes('falls asleep')
    ) {

        sleepStart = minute;

    } else {

        sleepMinutes[guard] +=
            minute - sleepStart;

        for (
            let m = sleepStart;
            m < minute;
            m++
        ) {
            minuteCount[guard][m]++;
        }
    }
}

let sleepiestGuard =
    Object.keys(sleepMinutes)
        .reduce((a, b) =>
            sleepMinutes[a] >
            sleepMinutes[b]
                ? a
                : b
        );

let bestMinute = 0;
let maxCount = 0;

for (let i = 0; i < 60; i++) {

    if ( minuteCount[sleepiestGuard][i] > maxCount )
    {
        maxCount = minuteCount[sleepiestGuard][i];

        bestMinute = i;
    }
}

console.log(
    Number(sleepiestGuard) * bestMinute
);
```
- This solves the Part 01 of this challenge.
