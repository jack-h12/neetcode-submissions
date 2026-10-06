class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                total += nums_dict[nums[i]]
                nums_dict[nums[i]] += 1
        return total
                