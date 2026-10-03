class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            total_h = 0

            for pile in piles:
                total_h += (pile + mid - 1) // mid

            if total_h <= h:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1
        return ans