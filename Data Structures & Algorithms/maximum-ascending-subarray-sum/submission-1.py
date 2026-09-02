class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_ascending = 1
        curr_streak = 1
        curr_sum = nums[0]
        max_sum = nums[0]
        prev_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev_num:
                curr_streak += 1
                curr_sum += nums[i]
                if curr_sum > max_sum:
                    max_sum = curr_sum
            else:
                curr_streak = 1
                curr_sum = nums[i]
            prev_num = nums[i]
        return max_sum