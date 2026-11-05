class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        if right < 2 or left > right:
            return [-1, -1]

        x = bytearray([1]) * (right + 1)
        x[0] = x[1] = 0

        for i in range(2, int(right**0.5) + 1):
            if x[i]:
                x[i * i : right + 1 : i] = bytearray(
                    (right - i * i) // i + 1
                )

        prev = -1
        min_diff = float("inf")
        ans = [-1, -1]

        for num in range(max(2, left), right + 1):
            if x[num]:
                if prev != -1:
                    diff = num - prev
                    if diff < min_diff:
                        min_diff = diff
                        ans = [prev, num]
                    if diff <= 2:
                        return ans
                prev = num

        return ans