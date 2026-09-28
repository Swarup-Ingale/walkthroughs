class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        b = []
        while n != 0 or i < j:
            if height[i] <= height[j]:
                b.append((j - i) * height[i])
                i += 1
            elif height[i] > height[j]:
                b.append((j - i) * height[j])
                j -= 1
            n -= 1
        return max(b)