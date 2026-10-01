class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1