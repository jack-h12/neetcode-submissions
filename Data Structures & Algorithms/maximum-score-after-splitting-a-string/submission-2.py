class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        ones_sum = 0
        curr_zeros_sum = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones_sum += 1
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones_sum -= 1
            else:
                curr_zeros_sum += 1
            if ones_sum + curr_zeros_sum > max_score:
                    max_score = ones_sum + curr_zeros_sum
        return max_score