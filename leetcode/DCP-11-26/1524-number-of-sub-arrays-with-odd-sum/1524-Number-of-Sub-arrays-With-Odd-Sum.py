class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        e_c = 1
        o_c = 0

        curr_parity = 0
        ans = 0

        for n in arr:
            curr_parity ^= (n & 1)
            if curr_parity == 1:
                ans += e_c
                o_c += 1
            else:
                ans += o_c
                e_c += 1
        
        return ans % MOD