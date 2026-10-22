class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        idx = nums.index(0)

        is_forward = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_forward = False
                break

        is_backward = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] - 1) % n:
                is_backward = False
                break

        ans = float('inf')

        if is_forward:
            ans = min(ans, idx, n - idx + 2)
        if is_backward:
            ans = min(ans, n - idx, idx + 2)

        return ans if ans != float('inf') else -1