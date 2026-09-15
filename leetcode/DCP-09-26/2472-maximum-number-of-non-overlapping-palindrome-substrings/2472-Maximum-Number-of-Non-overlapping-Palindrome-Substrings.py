class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        intervals = []
        n = len(s)

        for i in range(n - k + 1):
            sub = s[i:i+k]
            if sub == sub[::-1]:
                intervals.append((i, i + k - 1))

        for i in range(n - k):
            sub = s[i:i+k+1]
            if sub == sub[::-1]:
                intervals.append((i, i + k))

        intervals.sort(key=lambda x: (x[1], -x[0]))
        count = 0
        last_end = -1

        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count