import bisect
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for num in arr1:
            idx = bisect.bisect_left(arr2, num)

            if idx < len(arr2) and abs(arr2[idx] - num) <= d:
                continue

            if idx > 0 and abs(arr2[idx - 1] - num) <= d:
                continue

            distance_value += 1
            
        return distance_value