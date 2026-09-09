class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        output = []
        for i in range(len(nums)):
            if (i + 1) not in nums_set:
                output.append(i + 1)
        return output