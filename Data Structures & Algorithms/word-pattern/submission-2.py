class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != lst[i]:
                    return False
            else:
                if lst[i] in d.values():
                    return False
                d[pattern[i]] = lst[i]
        return True