class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parantheses = []
        pair = [0] * n

        for i in range(n):
            if s[i] == "(":
                open_parantheses.append(i)
            if s[i] == ")":
                j = open_parantheses.pop()
                pair[i] = j
                pair[j] = i

        r = []
        curr_idx = 0
        direction = 1
        
        while curr_idx < n:
            if s[curr_idx] == "(" or s[curr_idx] == ")":
                curr_idx = pair[curr_idx]
                direction = -direction
            else:
                r.append(s[curr_idx])
            curr_idx += direction
        
        return "".join(r)