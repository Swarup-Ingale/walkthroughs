from functools import cmp_to_key

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1

        div_count_by_factor = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] == 0:
                continue
            total_mult = 0
            for mult in range(2 * f, n + 1, f):
                total_mult += freq[mult]
            div_count_by_factor[f] = total_mult + (freq[f] - 1)

        options: list[tuple[int, int, int]] = []
        for factor, price in items:
            cnt = div_count_by_factor[factor]
            if cnt > 0:
                options.append((2, price, cnt))
            options.append((1, price, budget // price))

        def cmp(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
            g1, p1, _ = a
            g2, p2, _ = b
            left = g1 * p2
            right = g2 * p1
            if left != right:
                return -1 if left > right else 1
            return p1 - p2

        options.sort(key=cmp_to_key(cmp))

        rem_budget = budget
        total_copies = 0

        for gain, price, max_cnt in options:
            if rem_budget < price:
                continue
            can_buy = min(max_cnt, rem_budget // price)
            total_copies += can_buy * gain
            rem_budget -= can_buy * price

        return total_copies