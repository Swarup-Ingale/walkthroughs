class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        
        for i, num in enumerate(nums):
            if num != i:
                if ans == -1:
                    ans = num
                else:
                    ans &= num

        return 0 if ans == -1 else ans