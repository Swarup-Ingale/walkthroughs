class Solution:
    def minInsertions(self, s: str) -> int:
        req = 0
        insertions = 0
        for c in s:
            if c == "(":
                if req % 2 != 0:
                    insertions += 1
                    req -= 1
                req += 2

            else:
                req -= 1
                if req < 0:
                    insertions += 1
                    req = 1
                
        return insertions + req