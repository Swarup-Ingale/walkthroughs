import itertools

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        max_area = 0.0

        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            if area > max_area:
                max_area = area

        return max_area