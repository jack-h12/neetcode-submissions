class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        else:
            nums_dict = {}
            for num in nums:
                if num not in nums_dict.keys():
                    nums_dict[num] = 1
                else:
                    nums_dict[num] += 1
            for num in nums_dict.keys():
                if nums_dict[num] % 2 != 0:
                    return False
            return True