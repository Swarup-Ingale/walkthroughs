class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        limit = 1000

        while n >= limit:
            total_commas += (n - limit + 1)
            limit *= 1000

        return total_commas