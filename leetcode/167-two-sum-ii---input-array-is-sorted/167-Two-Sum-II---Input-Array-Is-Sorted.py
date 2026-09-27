class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if not numbers:
            return None
        n = len(numbers)

        l = 0
        r = n - 1
        while n != 0:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                else:
                    l += 1