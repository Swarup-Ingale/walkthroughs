class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        sub_num = {0:1}
        t = c = 0

        for n in nums:
            t += n
            if t - k in sub_num:
                c += sub_num[t - k]
            sub_num[t] = 1 + sub_num.get(t, 0)
        
        return c