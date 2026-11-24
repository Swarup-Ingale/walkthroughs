from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def lcm(a: int, b: int) -> int:
            return (a // gcd(a, b)) * b

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = x if g == 0 else gcd(g, x)
                l = lcm(l, x)
                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans