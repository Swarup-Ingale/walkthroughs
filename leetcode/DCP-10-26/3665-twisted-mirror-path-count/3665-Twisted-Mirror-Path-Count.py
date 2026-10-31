from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        R = [[0] * n for _ in range(m)]
        D = [[0] * n for _ in range(m)]

        if n > 1:
            R[0][1] = 1
        if m > 1:
            D[1][0] = 1
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == m - 1 and j == n - 1:
                    continue
                    
                if grid[i][j] == 0:
                    total = (R[i][j] + D[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j+1] = (R[i][j+1] + total) % MOD
                    if i + 1 < m:
                        D[i+1][j] = (D[i+1][j] + total) % MOD
                else:
                    if i + 1 < m:
                        D[i+1][j] = (D[i+1][j] + R[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j+1] = (R[i][j+1] + D[i][j]) % MOD

        return (R[m-1][n-1] + D[m-1][n-1]) % MOD