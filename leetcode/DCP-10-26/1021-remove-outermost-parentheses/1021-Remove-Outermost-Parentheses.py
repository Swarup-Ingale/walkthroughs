class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r = []
        depth = 0
        for c in s:
            if c == "(":
                if depth > 0:
                    r.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    r.append(c)
        
        return "".join(r)