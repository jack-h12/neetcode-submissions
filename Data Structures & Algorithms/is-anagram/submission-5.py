class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_char_num_dict, t_char_num_dict = {}, {}
            for i in range(0, len(s)):
                s_char_num_dict[s[i]] = s_char_num_dict.get(s[i], 0) + 1
                t_char_num_dict[t[i]] = t_char_num_dict.get(t[i], 0) + 1
            if s_char_num_dict == t_char_num_dict:
                return True
            else:
                return False