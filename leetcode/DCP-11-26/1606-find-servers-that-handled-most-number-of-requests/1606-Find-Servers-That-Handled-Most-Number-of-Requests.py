import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        requests_handled = [0] * k
        available = list(range(k))
        heapq.heapify(available)
        
        used = []
        busy = []
        
        for i, (arr_time, duration) in enumerate(zip(arrival, load)):
            target = i % k

            if target == 0 and used:
                available.extend(used)
                heapq.heapify(available)
                used.clear()

            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)

                if server_id < target:
                    heapq.heappush(used, server_id)
                else:
                    heapq.heappush(available, server_id)

            if available:
                assigned_server = heapq.heappop(available)
            elif used:
                assigned_server = heapq.heappop(used)
            else:
                continue

            requests_handled[assigned_server] += 1
            heapq.heappush(busy, (arr_time + duration, assigned_server))

        max_requests = max(requests_handled)
        return [i for i, count in enumerate(requests_handled) if count == max_requests]