class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        longest_count = 1
        current_count = 1

        sorted_list_no_duplicates = []

        for i in range(len(nums)):
            if nums[i] not in sorted_list_no_duplicates:
                sorted_list_no_duplicates.append(nums[i])

        if len(sorted_list_no_duplicates) == 1:
            return 1
        for i in range(1, len(sorted_list_no_duplicates)):
            if sorted_list_no_duplicates[i] == sorted_list_no_duplicates[i-1] + 1:
                current_count += 1
            else:
                if current_count > longest_count:
                    longest_count = current_count
                    current_count = 1
                else:
                    current_count = 1
        if current_count > longest_count:
            longest_count = current_count
        return longest_count