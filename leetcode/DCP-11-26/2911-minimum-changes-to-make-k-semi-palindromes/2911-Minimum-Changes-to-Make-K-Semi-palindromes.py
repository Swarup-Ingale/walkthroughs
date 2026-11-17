class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                for d in divisors[length]:
                    changes = 0
                    group_len = length // d
                    for rem in range(d):
                        left, right = 0, group_len - 1
                        while left < right:
                            if s[i + rem + left * d] != s[i + rem + right * d]:
                                changes += 1
                            left += 1
                            right -= 1
                    if changes < min_changes:
                        min_changes = changes
                        
                cost[i][j] = min_changes

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    curr = dp[p - 1][i] + cost[i][j - 1]
                    if curr < dp[p][j]:
                        dp[p][j] = curr
                        
        return dp[k][n]