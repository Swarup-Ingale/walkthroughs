class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            char[s[right]] = char.get(s[right], 0) + 1

            max_len = max(max_len, char[s[right]])
            if (right - left + 1) - max_len > k:
                char[s[left]] -= 1
                left += 1

        return len(s) - left