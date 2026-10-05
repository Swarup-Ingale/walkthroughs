class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        score = 0

        for c in range(len(s)):
            if s[c] == "(":
                depth += 1
            else:
                depth -= 1
                if s[c - 1] == "(":
                    score += 1 << depth
        
        return score