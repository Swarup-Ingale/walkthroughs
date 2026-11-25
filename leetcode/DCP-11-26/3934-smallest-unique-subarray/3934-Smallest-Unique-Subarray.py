class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        MOD1, BASE1 = 1_000_000_007, 100_003
        MOD2, BASE2 = 1_000_000_009, 100_019

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            x = val + 1
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2
            h1[i + 1] = (h1[i] * BASE1 + x) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + x) % MOD2

        def get_hash(l: int, r: int) -> tuple[int, int]:
            length = r - l
            v1 = (h1[r] - h1[l] * p1[length]) % MOD1
            v2 = (h2[r] - h2[l] * p2[length]) % MOD2
            return (v1, v2)

        def has_unique_of_len(length: int) -> bool:
            seen: dict[tuple[int, int], int] = {}
            for i in range(n - length + 1):
                key = get_hash(i, i + length)
                seen[key] = seen.get(key, 0) + 1
            return any(cnt == 1 for cnt in seen.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans