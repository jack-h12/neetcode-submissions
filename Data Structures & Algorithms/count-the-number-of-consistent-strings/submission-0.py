class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_char_set = set(allowed)
        consistent_strings = 0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed_char_set:
                    break
                if j == len(words[i]) - 1:
                    consistent_strings += 1
        return consistent_strings
