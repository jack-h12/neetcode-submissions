class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            res[tuple(char_count)] = res.get(tuple(char_count), []) + [string]
        return list(res.values())
