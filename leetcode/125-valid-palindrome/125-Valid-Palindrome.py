class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if i.isalnum())
        n = len(s)
        s = s.lower()
        if not s:
            return True
        
        i = 0
        while n != 0:
            if i < n - 1:
                if s[i] != s[n - 1]:
                    return False
            i += 1
            n -= 1

        return True