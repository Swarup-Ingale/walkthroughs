class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        moves = 0

        for i in range(len(nums)):
            moves += abs(nums[0] - nums[i])
        
        return moves