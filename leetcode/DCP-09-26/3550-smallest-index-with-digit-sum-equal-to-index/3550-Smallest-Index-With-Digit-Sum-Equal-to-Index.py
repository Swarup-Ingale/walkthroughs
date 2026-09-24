class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        b = []
        for i in range(len(nums)):
            a = 0
            x = nums[i]
            while x > 0:
                a += x % 10
                x = x // 10
            b.append(a)

        for j in range(len(b)):
            if b[j] == j:
                return j

        return -1