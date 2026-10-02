class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        
        def backtrack(s: str, o: int, c: int):
            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if o < n:
                backtrack(s + "(", o + 1, c)
            if c < o:
                backtrack(s + ")", o, c + 1)

        backtrack("", 0, 0)
        return ans