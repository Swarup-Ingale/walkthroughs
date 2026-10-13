from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort(reverse=True)

        p = (len(nums) + 1) // 2

        return sum(squares[:p]) - sum(squares[p:])