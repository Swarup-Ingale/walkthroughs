class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        x = bytearray([1]) * n
        x[0] = x[1] = 0

        x[4:n:2] = bytearray((n - 5) // 2 + 1)

        for i in range(3, int(n ** 0.5) + 1, 2):
            if x[i]:
                x[i * i : n : 2 * i] = bytearray((n - 1 - i * i) // (2 * i) + 1)
    
        return sum(x)