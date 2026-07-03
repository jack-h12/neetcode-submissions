class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_frequency = [0] * 26
        for c in s1:
            s1_char_frequency[ord(c) - ord('a')] += 1

        l, r = 0, len(s1) - 1
        for r in range(r, len(s2)):
            s2_char_frequency = [0] * 26
            for c in s2[l:r+1]:
                s2_char_frequency[ord(c) - ord('a')] += 1
            if s2_char_frequency == s1_char_frequency:
                return True
            l += 1
        return False
