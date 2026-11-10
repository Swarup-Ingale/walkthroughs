from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            step_cost = costs[i - 1]

            ans = dp[i - 1] + step_cost + 1

            if i >= 2:
                ans = min(ans, dp[i - 2] + step_cost + 4)

            if i >= 3:
                ans = min(ans, dp[i - 3] + step_cost + 9)
                
            dp[i] = ans
            
        return dp[n]