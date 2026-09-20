class Solution:
    def check(self, nums: List[int]) -> bool:
        num_of_decreases = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                num_of_decreases += 1
                if num_of_decreases > 1:
                    return False
        return True