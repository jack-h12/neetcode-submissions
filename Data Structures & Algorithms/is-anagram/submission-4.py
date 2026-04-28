class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_chars = {}
            for char in s:
                count_chars[char] = count_chars.get(char, 0) + 1
            for char in t:
                if char not in count_chars:
                    return False
                else:
                    count_chars[char] -= 1
                    if count_chars[char] == 0:
                        del count_chars[char]
            return len(count_chars) == 0