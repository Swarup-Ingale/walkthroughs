class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        for i in range(1, k + 1):
            dist[0][i] = 0

        pq = [(0, 0, 1)]
        
        while pq:
            w, u, c = heapq.heappop(pq)

            if w > dist[u][c]:
                continue

            if u == n - 1:
                return w

            for v, edge_w in adj[u]:
                nxt_w = w + edge_w

                if labels[v] == labels[u]:
                    nxt_c = c + 1
                else:
                    nxt_c = 1

                if nxt_c <= k:
                    if nxt_w < dist[v][nxt_c]:
                        for i in range(nxt_c, k + 1):
                            if nxt_w < dist[v][i]:
                                dist[v][i] = nxt_w
                            else:
                                break
                                
                        heapq.heappush(pq, (nxt_w, v, nxt_c))

        return -1