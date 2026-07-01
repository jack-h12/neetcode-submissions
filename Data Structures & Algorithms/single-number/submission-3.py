class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp_num = nums[i]
            nums[i] = "a"
            if temp_num not in nums:
                return temp_num
            nums[i] = temp_num