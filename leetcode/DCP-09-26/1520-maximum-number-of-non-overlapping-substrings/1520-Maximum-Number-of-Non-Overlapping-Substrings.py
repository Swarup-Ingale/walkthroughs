class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        L = {}
        R = {}
        for i, char in enumerate(s):
            if char not in L:
                L[char] = i
            R[char] = i

        valid_intervals = []

        for char in L:
            i = L[char]
            j = R[char]
            k = i
            is_valid = True

            while k <= j:
                curr_char = s[k]
                if L[curr_char] < i:
                    is_valid = False
                    break

                j = max(j, R[curr_char])
                k += 1

            if is_valid:
                valid_intervals.append((i, j))

        valid_intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        last_end = -1

        for start, end in valid_intervals:
            if start > last_end:
                ans.append(s[start:end + 1])
                last_end = end
        return ans