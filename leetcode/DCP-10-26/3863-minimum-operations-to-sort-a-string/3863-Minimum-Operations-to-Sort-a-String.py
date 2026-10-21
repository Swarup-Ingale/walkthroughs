class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                break
        if is_sorted:
            return 0

        min_char = min(s)
        max_char = max(s)
        
        if s[0] == min_char or s[-1] == max_char:
            return 1

        if n <= 2:
            return -1

        if s[0] == max_char and s[-1] == min_char:
            if s.count(max_char) == 1 and s.count(min_char) == 1:
                return 3

        return 2