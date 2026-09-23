class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_dict = {}
        for i in range(len(arr)):
            if arr[i] not in num_dict.keys():
                num_dict[arr[i]] = 1
            else:
                num_dict[arr[i]] += 1
        
        largest_lucky_int = -1
        for key in num_dict.keys():
            if key == num_dict[key]:
                if key > largest_lucky_int:
                    largest_lucky_int = key
        
        return largest_lucky_int