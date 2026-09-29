from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] != "(" or grid[m - 1][n - 1] != ")":
            return False

        memo = {}

        def dfs(r: int, c: int, b: int) -> bool:
            if b < 0:
                return False

            sr = (m - 1 - r) + (n - 1 - c)
            if b > sr:
                return False

            if r == m - 1 and c == n - 1:
                return b == 0

            s = (r, c, b)
            if s in memo:
                return memo[s]

            if c + 1 < n:
                ch = 1 if grid[r][c + 1] == "(" else -1
                if dfs(r, c + 1, b + ch):
                    return True

            if r + 1 < m:
                ch = 1 if grid[r + 1][c] == "(" else -1
                if dfs(r + 1, c, b + ch):
                    return True

            memo[s] = False
            return False

        return dfs(0, 0, 1)