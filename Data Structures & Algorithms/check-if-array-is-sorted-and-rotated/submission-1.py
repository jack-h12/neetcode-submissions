class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            first_num = sorted_nums.pop(0)
            sorted_nums.append(first_num)
            if sorted_nums == nums:
                return True
        return False