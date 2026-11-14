class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        min_sum = float('inf')

        for i in range(n - l + 1):
            max_j = min(n - 1, i + r - 1)
            for j in range(i + l - 1, max_j + 1):
                curr_sum = pref[j + 1] - pref[i]
                if curr_sum > 0 and curr_sum < min_sum:
                    min_sum = curr_sum
                    
        return min_sum if min_sum != float('inf') else -1