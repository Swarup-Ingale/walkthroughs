class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)

        busy_servers = []
        ans = []
        curr_time = 0
        
        for j, duration in enumerate(tasks):
            curr_time = max(curr_time, j)

            if not free_servers:
                curr_time = max(curr_time, busy_servers[0][0])

            while busy_servers and busy_servers[0][0] <= curr_time:
                time_free, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))

            best_weight, best_idx = heapq.heappop(free_servers)
            ans.append(best_idx)

            heapq.heappush(busy_servers, (curr_time + duration, best_weight, best_idx))
            
        return ans