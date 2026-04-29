class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in pairs:
                return [min(i, pairs.get(difference, 0)), max(i, pairs.get(difference, 0))]
            else:
                pairs[nums[i]] = i
