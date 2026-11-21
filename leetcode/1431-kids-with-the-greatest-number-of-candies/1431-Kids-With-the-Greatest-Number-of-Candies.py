class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        mx = max(candies)
        return [c + extraCandies >= mx for c in candies]