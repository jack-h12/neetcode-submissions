class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        current_streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
                max_consecutive_ones = max(max_consecutive_ones, current_streak)
            else:
                current_streak = 0
        return max_consecutive_ones