class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_q = sorted([(q, i) for i, q in enumerate(queries)])

        result = [0] * len(queries)
        server_counts = [0] * (n + 1)
        active_servers = 0

        left = right = 0

        for q, idx in sorted_q:
            while right < len(logs) and logs[right][1] <= q:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    active_servers += 1
                server_counts[server_id] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1

            result[idx] = n - active_servers

        return result