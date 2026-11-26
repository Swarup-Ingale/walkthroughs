from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        return sum(row_counts[col] for col in zip(*grid))