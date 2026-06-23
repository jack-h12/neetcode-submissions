import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            curr_num = nums[i]
            nums[i] = 1
            output.append(math.prod(nums))
            nums[i] = curr_num
        return output