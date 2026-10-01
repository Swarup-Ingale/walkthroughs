class Solution:
    def isValid(self, s: str) -> bool:
        a = {")": "(", "}": "{", "]": "["}
        b = []

        for c in s:
            if c in a:
                top = b.pop() if b else "#"
                
                if a[c] != top:
                    return False

            else:
                b.append(c)
        
        return not b