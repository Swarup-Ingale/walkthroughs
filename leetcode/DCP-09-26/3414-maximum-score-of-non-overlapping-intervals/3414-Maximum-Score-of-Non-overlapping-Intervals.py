class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        intervals_with_idx = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]

        intervals_with_idx.sort(key = lambda x: x[0])
        starts = [x[0] for x in intervals_with_idx]

        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect_right(starts, intervals_with_idx[i][1])

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            weight = intervals_with_idx[i][2]
            orig_id = intervals_with_idx[i][3]
            nxt = next_idx[i]

            for k in range(1, 5):
                best_w, best_l = dp[i + 1][k]
                inc_w = weight + dp[nxt][k - 1][0]
                inc_l = sorted(dp[nxt][k - 1][1] + [orig_id])

                if inc_w > best_w:
                    dp[i][k] = (inc_w, inc_l)
                
                elif inc_w == best_w:
                    if inc_l < best_l:
                        dp[i][k] = (inc_w, inc_l)
                    else:
                        dp[i][k] = (best_w, best_l)

                else:
                    dp[i][k] = (best_w, best_l)

        return dp[0][4][1]