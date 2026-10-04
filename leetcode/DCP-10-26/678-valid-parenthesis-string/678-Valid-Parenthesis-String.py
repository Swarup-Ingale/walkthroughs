class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0

        for c in s:
            if c == "(":
                cmin += 1
                cmax += 1
            elif c == ")":
                cmin -= 1
                cmax -= 1
            elif c == "*":
                cmin -= 1
                cmax += 1
        
            if cmax < 0:
                return False
            
            cmin = max(cmin, 0)
        return cmin == 0