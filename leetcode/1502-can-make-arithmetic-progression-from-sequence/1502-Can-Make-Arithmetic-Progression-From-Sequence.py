class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]

        for c in range(2, len(arr)):
            if arr[c] - arr[c - 1] != d:
                return False
        
        return True