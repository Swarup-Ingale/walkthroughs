class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            a[tuple(count)].append(s)

        return list(a.values())