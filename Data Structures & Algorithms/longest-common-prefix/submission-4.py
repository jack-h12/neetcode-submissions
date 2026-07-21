class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        for i in range(0, len(strs[0])):
            curr_prefix = strs[0][:i+1]
            curr_prefix_works = True
            for j in range(len(strs)):
                if curr_prefix != strs[j][:i+1]:
                    curr_prefix_works = False
                    break
            if curr_prefix_works == True:
                longest_prefix = curr_prefix
        return longest_prefix
                
