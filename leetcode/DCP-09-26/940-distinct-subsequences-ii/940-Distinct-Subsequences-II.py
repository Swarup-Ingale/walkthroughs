class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        ends_with = [0] * 26
        total = 0

        for char in s:
            idx = ord(char) - 97
            old_count = ends_with[idx]
            new_count = (total + 1) % MOD
            total = (total - old_count + new_count) % MOD
            ends_with[idx] = new_count

        return total