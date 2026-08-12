class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd_freq = 0
        min_even_freq = len(s)
        nums_dict = {}
        for i in range(len(s)):
            # adding or incrementing current letter's count in dictionary
            if s[i] not in nums_dict.keys():
                nums_dict[s[i]] = 1
            else:
                nums_dict[s[i]] += 1

        for count in nums_dict.values():
            # if the count is even, update max_even_freq
            if count % 2 == 0:
                if count < min_even_freq:
                    min_even_freq = count
            else: # if odd, update max_odd_freq
                if count > max_odd_freq:
                    max_odd_freq = count

        return max_odd_freq - min_even_freq