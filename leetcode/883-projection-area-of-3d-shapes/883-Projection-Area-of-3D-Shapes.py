class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)

        xy = sum(1 for r in range(n) for c in range(n) if grid[r][c] > 0)

        zx = sum(max(row) for row in grid)

        yz = sum(max(grid[r][c] for r in range(n)) for c in range(n))

        return xy + zx + yz