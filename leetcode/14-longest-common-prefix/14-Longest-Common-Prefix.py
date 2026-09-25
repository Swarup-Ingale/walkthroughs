class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        first = min(strs)
        last = max(strs)

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return first[:i]

        return first[:min(len(first), len(last))]