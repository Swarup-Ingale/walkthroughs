class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        l = 0
        
        for start in num_set:
            if start - 1 not in num_set:
                end = start + 1
                while end in num_set:
                    end += 1
                l = max(l, end - start)

        return l