class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest_subarray_increasing_or_decreasing = 0
        curr_streak = 1
        has_been_increasing = True
        has_been_decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if has_been_increasing == True:
                    curr_streak += 1
                else:
                    curr_streak = 2
                has_been_increasing = True
                has_been_decreasing = False
            elif nums[i] < nums[i - 1]:
                if has_been_decreasing == True:
                    curr_streak += 1
                else:
                    curr_streak = 2
                has_been_decreasing = True
                has_been_increasing = False
            else:
                curr_streak = 1
                has_been_decreasing = False
                has_been_increasing = False
            if curr_streak > longest_subarray_increasing_or_decreasing:
                longest_subarray_increasing_or_decreasing = curr_streak
        return longest_subarray_increasing_or_decreasing
            