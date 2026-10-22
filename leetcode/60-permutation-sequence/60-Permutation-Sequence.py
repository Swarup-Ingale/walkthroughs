class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
        digits = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []

        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            result.append(digits[idx])
            digits.pop(idx)
            k %= factorials[i]

        return "".join(result)