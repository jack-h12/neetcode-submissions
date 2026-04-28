class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_char_num_dict = {}
            t_char_num_dict = {}
            for i in range(0, len(s)):
                if s[i] in s_char_num_dict:
                    s_char_num_dict[s[i]] += 1
                else:
                    s_char_num_dict[s[i]] = 1
                if t[i] in t_char_num_dict:
                    t_char_num_dict[t[i]] += 1
                else:
                    t_char_num_dict[t[i]] = 1
            if s_char_num_dict == t_char_num_dict:
                return True
            else:
                return False