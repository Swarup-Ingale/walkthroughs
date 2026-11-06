class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        i = 1

        while i <= n:
            m = i * 10
            count += (n // m) * i
            count += min(max(n % m - i + 1, 0), i)
            i *= 10

        return count