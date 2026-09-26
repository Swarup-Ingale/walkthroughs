class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_max, max_till_now = 0, -inf
        for i in nums:
            curr_max = max(i, curr_max + i)
            max_till_now = max(max_till_now, curr_max)
        return max_till_now