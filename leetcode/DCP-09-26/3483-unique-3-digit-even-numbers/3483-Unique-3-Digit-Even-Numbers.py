class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = [0] * 10
        for digit in digits:
            counts[digit] += 1

        valid_count = 0

        for i in range(100, 999, 2):
            ones = i % 10
            tens = (i // 10) % 10
            hundreds = i // 100

            counts[ones] -= 1
            counts[tens] -= 1
            counts[hundreds] -= 1

            if counts[ones] >= 0 and counts[tens] >= 0 and counts[hundreds] >= 0:
                valid_count += 1

            counts[ones] += 1
            counts[tens] += 1
            counts[hundreds] += 1

        return valid_count