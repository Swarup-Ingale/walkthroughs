class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current_vowels = sum(1 for ch in s[:k] if ch in vowels)
        max_vowels = current_vowels

        for a in range(k, len(s)):
            if s[a] in vowels:
                current_vowels += 1
            if s[a - k] in vowels:
                current_vowels -= 1

            if current_vowels > max_vowels:
                max_vowels = current_vowels
                if max_vowels == k:
                    return k
            
        return max_vowels