class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round = []

            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                chunk_sum = sum(int(ch) for ch in chunk)
                next_round.append(str(chunk_sum))

            s = "".join(next_round)
            
        return s