class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        curr_substring_chars = set()
        for r in range(len(s)):
            while s[r] in curr_substring_chars:
                curr_substring_chars.remove(s[l])
                l += 1
            curr_substring_chars.add(s[r])
            if r - l + 1 > max_length:
                max_length = r - l + 1
        return max_length
