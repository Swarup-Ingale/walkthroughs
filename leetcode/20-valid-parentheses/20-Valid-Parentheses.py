class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack:
                    a = stack.pop()
                    if (c == ")" and a == "(") or (c == "]" and a == "[") or (c == "}" and a == "{"):
                        continue
                    else:
                        return False
                else:
                    return False
        
        return not stack