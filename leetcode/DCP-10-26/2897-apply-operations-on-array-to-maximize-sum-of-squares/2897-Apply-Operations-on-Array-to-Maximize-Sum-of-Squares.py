from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30

        for num in nums:
            for b in range(30):
                if (num >> b) & 1:
                    bit_counts[b] += 1
                    
        ans = 0

        for _ in range(k):
            curr = 0
            for b in range(30):
                if bit_counts[b] > 0:
                    curr |= (1 << b)
                    bit_counts[b] -= 1

            if curr == 0:
                break
                
            ans = (ans + curr * curr) % MOD
            
        return ans