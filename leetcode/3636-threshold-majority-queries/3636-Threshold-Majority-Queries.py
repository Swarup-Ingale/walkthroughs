from bisect import bisect_left

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)

        unique_vals = sorted(set(nums))
        m = len(unique_vals)
        comp = [bisect_left(unique_vals, x) for x in nums]

        block_size = max(1, int(n / (q ** 0.5)))
        indexed_queries = []
        for idx, (l, r, thresh) in enumerate(queries):
            indexed_queries.append((l // block_size, r, l, thresh, idx))

        indexed_queries.sort(key = lambda x: (x[0], x[1] if x[0] % 2 == 0 else -x[1]))

        freq = [0] * m
        freq_count = [0] * (n + 1)
        max_freq = 0

        def add(idx):
            nonlocal max_freq
            val = comp[idx]
            f = freq[val]
            if f > 0:
                freq_count[f] -= 1
            f += 1
            freq[val] = f
            freq_count[f] += 1
            if f > max_freq:
                max_freq = f

        def remove(idx):
            nonlocal max_freq
            val = comp[idx]
            f = freq[val]
            freq_count[f] -= 1
            f -= 1
            freq[val] = f
            if f > 0:
                freq_count[f] += 1
            if freq_count[max_freq] == 0:
                max_freq -= 1

        ans = [-1] * q
        curr_l, curr_r = 0, -1

        for _, r, l, thresh, q_idx in indexed_queries:
            while curr_l > l:
                curr_l -= 1
                add(curr_l)
            while curr_r < r:
                curr_r += 1
                add(curr_r)
            while curr_l < l:
                remove(curr_l)
                curr_l += 1
            while curr_r > r:
                remove(curr_r)
                curr_r -= 1

            if max_freq >= thresh:
                for val in range(m):
                    if freq[val] == max_freq:
                        ans[q_idx] = unique_vals[val]
                        break

        return ans