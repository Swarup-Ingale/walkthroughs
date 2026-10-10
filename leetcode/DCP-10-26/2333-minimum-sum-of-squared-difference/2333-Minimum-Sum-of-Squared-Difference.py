class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if k >= sum(diffs):
            return 0
        
        max_d = max(diffs)
        count = [0] * (max_d + 1)

        for d in diffs:
            count[d] += 1
        
        for d in range(max_d, 0, -1):
            if count[d] > 0:
                if k >= count[d]:
                    k -= count[d]
                    count[d - 1] += count[d]
                    count[d] = 0
                else:
                    count[d - 1] += k
                    count[d] -= k
                    k = 0
                    break 

        ans = 0
        for d in range(1, max_d + 1):
            if count[d] > 0:
                ans += count[d] * (d ** 2)
                
        return ans