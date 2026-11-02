class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        target_idx = len(nums) // 2
        moves = 0

        for i in range(len(nums)):
            moves += abs(nums[i] - nums[target_idx])

        return moves