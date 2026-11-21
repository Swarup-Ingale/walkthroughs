class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        stack = [(0, 0, -1)]
        while stack:
            u, state, prev = stack.pop()
            c = ord(s[u]) - ord('a')
            if state == 0:
                if u != 0 and last_seen[c] != -1:
                    new_parent[u] = last_seen[c]
                stack.append((u, 1, last_seen[c]))
                last_seen[c] = u
                for v in reversed(adj[u]):
                    stack.append((v, 0, -1))
            else:
                last_seen[c] = prev

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [1] * n
        order = []
        dfs_stack = [0]
        while dfs_stack:
            u = dfs_stack.pop()
            order.append(u)
            for v in new_adj[u]:
                dfs_stack.append(v)

        for u in reversed(order):
            for v in new_adj[u]:
                ans[u] += ans[v]

        return ans