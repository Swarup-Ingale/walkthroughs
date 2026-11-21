class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        q = max(m, n)
        res = []

        for i in range(q):
            if i < m:
                res.append(word1[i])
            if i < n:
                res.append(word2[i])

        return "".join(res)