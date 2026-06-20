class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] == 0:
                pass
            elif nums[i] != 0 and ((nums[i] - 1) not in nums):
                return nums[i] - 1
        return len(nums)