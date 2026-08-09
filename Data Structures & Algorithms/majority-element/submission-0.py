class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = {}
        for i in range(len(nums)):
            if nums[i] not in nums_count.keys():
                nums_count[nums[i]] = 1
            else:
                nums_count[nums[i]] += 1
            if nums_count[nums[i]] > len(nums) // 2:
                return nums[i]
        return