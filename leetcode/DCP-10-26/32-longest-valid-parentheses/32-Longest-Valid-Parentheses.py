class Solution:
    def longestValidParentheses(self, s: str) -> int:
        a = [-1]
        max_len = 0

        for i, c in enumerate(s):
            if c == "(":
                a.append(i)

            else:
                a.pop()
                if not a:
                    a.append(i)
                else:
                    curr_len = i - a[-1]
                    max_len = max(max_len, curr_len)

        return max_len