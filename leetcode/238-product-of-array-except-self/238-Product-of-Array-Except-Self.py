class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        o = [1] * len(nums)
        l = 1

        for i in range(len(nums)):
            o[i] *= l
            l *= nums[i]
        
        r = 1

        for i in range(len(nums) - 1, -1, -1):
            o[i] *= r
            r *= nums[i]
        
        return o