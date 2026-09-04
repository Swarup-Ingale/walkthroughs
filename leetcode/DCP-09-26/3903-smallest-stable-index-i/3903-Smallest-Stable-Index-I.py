class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        min_suff = [0] * n
        min_suff[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            min_suff[i] = min(nums[i], min_suff[i + 1])

        max_pref = -float('inf')

        for i in range(n):
            max_pref = max(max_pref, nums[i])
            if max_pref - min_suff[i] <= k:
                return i

        return -1