from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        valid_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_sum = grid[r][c]
                    grid[r][c] = 0

                    queue = deque([(r, c)])

                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                queue.append((nr, nc))

                    if island_sum % k == 0:
                        valid_islands += 1

        return valid_islands