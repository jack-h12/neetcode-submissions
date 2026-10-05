class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        smallest = min(nums[0], nums[1])
        second_smallest = max(nums[0], nums[1])
        for i in range(len(nums)):
            if nums[i] > biggest:
                if biggest != 0:
                    second_biggest = biggest
                biggest = nums[i]
            elif nums[i] > second_biggest:
                second_biggest = nums[i]
            elif nums[i] < smallest:
                second_smallest = smallest
                smallest = nums[i]
            elif nums[i] < second_smallest:
                second_smallest = nums[i]
        return (biggest * second_biggest) - (smallest * second_smallest)