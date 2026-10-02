class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = {}
        c2 = {}

        for i in range(len(s1)):
            c1[s1[i]] = c1.get(s1[i], 0) + 1
            c2[s2[i]] = c2.get(s2[i], 0) + 1
        
        if c1 == c2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            c2[s2[right]] = c2.get(s2[right], 0) + 1
            c2[s2[left]] -= 1

            if c2[s2[left]] == 0:
                del c2[s2[left]]
            
            left += 1

            if c1 == c2:
                return True

        return False