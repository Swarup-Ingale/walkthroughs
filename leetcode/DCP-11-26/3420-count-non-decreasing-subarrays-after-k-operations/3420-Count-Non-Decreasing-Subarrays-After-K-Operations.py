import bisect
from typing import List

class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 2)
        self.size = size
        
    def add(self, i: int, delta: int):
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)
            
    def range_add(self, l: int, r: int, delta: int):
        self.add(l, delta)
        self.add(r + 1, -delta)
        
    def query(self, i: int) -> int:
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        fenwick = FenwickTree(n)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        stack = []
        stack_starts = []
        
        ans = 0
        L = 0
        
        for R in range(n):
            val = nums[R]
            start_L = R

            while stack and stack[-1][0] <= val:
                popped = stack.pop()
                stack_starts.pop()

                duration = R - popped[3]
                added_contrib = popped[0] * duration
                fenwick.range_add(popped[1], popped[2], added_contrib)

                start_L = popped[1]

            stack.append((val, start_L, R, R))
            stack_starts.append(start_L)

            while L <= R:
                idx = bisect.bisect_right(stack_starts, L) - 1
                block = stack[idx]

                committed = fenwick.query(L)
                active = block[0] * (R - block[3] + 1)
                sum_max = committed + active

                cost = sum_max - (pref[R + 1] - pref[L])
                
                if cost <= k:
                    break
                    
                L += 1

            ans += R - L + 1
            
        return ans