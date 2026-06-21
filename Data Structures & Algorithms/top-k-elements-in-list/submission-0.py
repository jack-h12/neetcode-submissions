class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        output_list = []
        for i in range(k):
            most_frequent = max(dictionary, key=dictionary.get)
            output_list.append(most_frequent)
            del dictionary[most_frequent]
        return output_list