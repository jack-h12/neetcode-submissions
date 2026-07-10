class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        summ = 0
        while i < len(s) - 1:
            summ = summ + abs(ord(s[i+1]) - ord(s[i]))
            i += 1
        return summ