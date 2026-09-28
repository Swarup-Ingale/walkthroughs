class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        j = 0
        for i in s:
            if i == "(":
                c += 1
                j = max(c, j)
            elif i == ")":
                c -= 1
        return j