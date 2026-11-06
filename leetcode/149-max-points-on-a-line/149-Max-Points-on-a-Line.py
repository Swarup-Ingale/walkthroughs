import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 2

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1

                g = math.gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1

            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)

        return max_points