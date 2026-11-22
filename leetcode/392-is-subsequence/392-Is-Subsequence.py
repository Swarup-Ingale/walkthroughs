class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        a = 0
        count = 0

        for i in range(len(t)):
            if a < len(s) and s[a] == t[i]:
                count += 1
                a += 1

        if len(s) == count:
            return True
        else:
            return False