class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        x = math.isqrt(total_sum)
        if x * x == total_sum:
            return x
            
        return -1