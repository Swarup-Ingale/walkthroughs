class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free_cnt = [0] * n

        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            free_cnt[i] = cnt

        min_price = min(price for _, price in items)

        dp = [0] * (budget + 1)
        for i in range(n):
            _, price = items[i]
            val = 1 + free_cnt[i]
            for c in range(budget, price - 1, -1):
                if dp[c - price] + val > dp[c]:
                    dp[c] = dp[c - price] + val

        ans = 0
        for spent in range(budget + 1):
            total = dp[spent] + (budget - spent) // min_price
            if total > ans:
                ans = total

        return ans