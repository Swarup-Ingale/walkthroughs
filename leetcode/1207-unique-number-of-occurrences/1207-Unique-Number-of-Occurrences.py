class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        ans = {}

        for i in arr:
            ans[i] = ans.get(i, 0) + 1
        
        unique = set(ans.values())
        return len(unique) == len(ans)