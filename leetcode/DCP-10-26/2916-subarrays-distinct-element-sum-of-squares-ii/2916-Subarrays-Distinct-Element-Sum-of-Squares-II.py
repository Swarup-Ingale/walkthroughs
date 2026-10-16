from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum_sq = [0] * (4 * n + 1)
        sum_val = [0] * (4 * n + 1)
        lazy = [0] * (4 * n + 1)
        
        def push_down(node: int, l: int, r: int):
            if lazy[node]:
                mid = (l + r) // 2
                left = node * 2
                right = node * 2 + 1
                v = lazy[node]
                
                len_left = mid - l + 1
                len_right = r - mid

                sum_sq[left] = (sum_sq[left] + 2 * v * sum_val[left] + v * v * len_left) % MOD
                sum_val[left] = (sum_val[left] + v * len_left) % MOD
                lazy[left] = (lazy[left] + v) % MOD

                sum_sq[right] = (sum_sq[right] + 2 * v * sum_val[right] + v * v * len_right) % MOD
                sum_val[right] = (sum_val[right] + v * len_right) % MOD
                lazy[right] = (lazy[right] + v) % MOD

                lazy[node] = 0

        def update(node: int, l: int, r: int, ql: int, qr: int, v: int):
            if ql <= l and r <= qr:
                length = r - l + 1
                sum_sq[node] = (sum_sq[node] + 2 * v * sum_val[node] + v * v * length) % MOD
                sum_val[node] = (sum_val[node] + v * length) % MOD
                lazy[node] = (lazy[node] + v) % MOD
                return

            push_down(node, l, r)
            mid = (l + r) // 2
            
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, v)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, v)

            sum_sq[node] = (sum_sq[node * 2] + sum_sq[node * 2 + 1]) % MOD
            sum_val[node] = (sum_val[node * 2] + sum_val[node * 2 + 1]) % MOD

        ans = 0
        last_seen = {}
        
        for j, num in enumerate(nums):
            start = last_seen.get(num, -1) + 1

            update(1, 0, n - 1, start, j, 1)

            ans = (ans + sum_sq[1]) % MOD
            
            last_seen[num] = j
            
        return ans