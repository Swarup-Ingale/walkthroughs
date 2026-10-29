class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        s_vals = [ord(c) - 97 for c in s]

        LOG = 16
        in_time = [0] * n
        out_time = [0] * n
        depth = [0] * n
        up = [[0] * LOG for _ in range(n)]
        point_query_initial = [0] * n
        
        timer = 0
        stack = [(0, 0, 0, 0, False)]
        
        while stack:
            u, p, d, mask, is_post = stack.pop()
            if is_post:
                out_time[u] = timer - 1
            else:
                in_time[u] = timer
                timer += 1
                depth[u] = d
                up[u][0] = p
                mask ^= (1 << s_vals[u])
                point_query_initial[in_time[u]] = mask

                stack.append((u, p, d, mask, True))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1, mask, False))

        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        bit = [0] * (n + 2)
        
        def add(idx: int, val: int):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx: int) -> int:
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def range_update(left: int, right: int, val: int):
            add(left, val)
            add(right + 1, val)

        last_val = 0
        for i in range(n):
            curr_val = point_query_initial[i]
            add(i, last_val ^ curr_val)
            last_val = curr_val

        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_char_val = ord(c) - 97

                val = (1 << s_vals[u]) ^ (1 << new_char_val)
                range_update(in_time[u], out_time[u], val)

                s_vals[u] = new_char_val
                
            elif parts[0] == "query":
                u = int(parts[1])
                v = int(parts[2])
                
                mask_u = query_bit(in_time[u])
                mask_v = query_bit(in_time[v])
                lca = get_lca(u, v)

                path_mask = mask_u ^ mask_v ^ (1 << s_vals[lca])

                can_be_palindrome = (path_mask & (path_mask - 1)) == 0
                answer.append(can_be_palindrome)
                
        return answer