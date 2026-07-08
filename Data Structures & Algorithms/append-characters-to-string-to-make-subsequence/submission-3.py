class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_pointer = 0
        s_pointer = 0
        while t_pointer < len(t) and s_pointer < len(s):
            if t[t_pointer] == s[s_pointer]:
                t_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1
        return len(t) - t_pointer