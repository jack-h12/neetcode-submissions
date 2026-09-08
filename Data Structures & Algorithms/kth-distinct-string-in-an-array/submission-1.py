class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strings_dict = {}
        k_num = 0
        for i in range(len(arr)):
            if arr[i] not in strings_dict.keys():
                strings_dict[arr[i]] = 1
            else:
                strings_dict[arr[i]] += 1
        for i in range(len(arr)):
            if strings_dict[arr[i]] == 1:
                k_num += 1
                if k_num == k:
                    return arr[i]
        return ""
            