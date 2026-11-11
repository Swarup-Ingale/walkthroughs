class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        opt1 = need1 * cost1 + need2 * cost2
        overlap = min(need1, need2)
        opt2 = (overlap * costBoth) + ((need1 - overlap) * cost1) + ((need2 - overlap) * cost2)
        opt3 = max(need1, need2) * costBoth
        return min(opt1, opt2, opt3)