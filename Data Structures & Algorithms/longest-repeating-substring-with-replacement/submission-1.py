class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_occurences = {}
        l = 0
        max_length = 0
        max_frequency = 0
        for r in range(len(s)):
            letter_occurences[s[r]] = 1 + letter_occurences.get(s[r], 0)
            max_frequency = max(max_frequency, letter_occurences[s[r]])
            while (r - l + 1) - max_frequency > k:
                letter_occurences[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
