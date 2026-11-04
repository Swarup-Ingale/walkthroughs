from typing import List

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        
    def add(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        unique_nums = sorted(list(set(nums)))
        U = len(unique_nums)
        rank = {v: i + 1 for i, v in enumerate(unique_nums)}
        val = {i + 1: v for i, v in enumerate(unique_nums)}
        
        count_BIT = FenwickTree(U)
        sum_BIT = FenwickTree(U)
        LOG = U.bit_length()
        
        def find_kth(target_k: int) -> int:
            curr = 0
            for i in range(LOG, -1, -1):
                next_idx = curr + (1 << i)
                if next_idx <= U and count_BIT.tree[next_idx] < target_k:
                    curr = next_idx
                    target_k -= count_BIT.tree[curr]
            return curr + 1

        cost = []
        window_sum = 0
        k_med = x // 2 + 1
        
        for i in range(n):
            v = nums[i]
            r = rank[v]
            count_BIT.add(r, 1)
            sum_BIT.add(r, v)
            window_sum += v

            if i >= x:
                out_v = nums[i - x]
                out_r = rank[out_v]
                count_BIT.add(out_r, -1)
                sum_BIT.add(out_r, -out_v)
                window_sum -= out_v

            if i >= x - 1:
                med_r = find_kth(k_med)
                M = val[med_r]
                
                c_low = count_BIT.query(med_r)
                s_low = sum_BIT.query(med_r)
                
                c_up = x - c_low
                s_up = window_sum - s_low
                
                window_cost = c_low * M - s_low + s_up - c_up * M
                cost.append(window_cost)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                best = dp[i - 1][j]

                if i >= x:
                    take_cost = dp[i - x][j - 1] + cost[i - x]
                    if take_cost < best:
                        best = take_cost
                        
                dp[i][j] = best
                
        return dp[n][k]