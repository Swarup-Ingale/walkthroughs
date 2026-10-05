class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        nge = {}

        for n in reversed(nums2):
            while stack and stack[-1] <= n:
                stack.pop()
            
            if stack:
                nge[n] = stack[-1]
            else:
                nge[n] = -1
            
            stack.append(n)
        
        return [nge[i] for i in nums1]