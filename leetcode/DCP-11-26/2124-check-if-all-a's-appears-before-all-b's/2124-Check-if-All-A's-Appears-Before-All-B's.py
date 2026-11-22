class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for ch in s:
            if ch == 'b':
                seen_b = True
            elif seen_b:
                return False
        return True