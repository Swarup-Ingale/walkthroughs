class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]

        dp[0].add(grid[0][0])

        for j in range(1, n):
            for val in dp[j-1]:
                dp[j].add(val ^ grid[0][j])

        for i in range(1, m):
            dp[0] = {val ^ grid[i][0] for val in dp[0]}

            for j in range(1, n):
                new_set = set()

                for val in dp[j-1]:
                    new_set.add(val ^ grid[i][j])

                for val in dp[j]:
                    new_set.add(val ^ grid[i][j])
                    
                dp[j] = new_set

        return min(dp[-1])