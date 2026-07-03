class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_frequency = [0] * 26
        s2_char_frequency = [0] * 26

        for c in s1:
            s1_char_frequency[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            s2_char_frequency[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                s2_char_frequency[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s2_char_frequency == s1_char_frequency:
                return True
        return False
