class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 0:
            return ""
        stack = []

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)