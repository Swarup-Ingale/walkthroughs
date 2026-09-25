class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()
        visited = set()

        def dfs(expr):
            if expr in visited:
                return 
            visited.add(expr)

            right = expr.find('}')
            if right == -1:
                res.add(expr)
                return

            left = expr.rfind('{', 0, right)
            inside = expr[left + 1 : right]
            pieces = inside.split(',')

            for piece in pieces:
                new_expr = expr[:left] + piece + expr[right + 1:]
                dfs(new_expr)

        dfs(expression)
        return sorted(list(res))