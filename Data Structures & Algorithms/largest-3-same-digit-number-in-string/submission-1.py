class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr_largest_good_num = ""
        for i in range(len(num) - 2):
            if num[i + 2] == num[i + 1] == num[i]:
                good_num = num[i:i+3]
                if curr_largest_good_num == "":
                    curr_largest_good_num = good_num
                else:
                    if int(good_num) > int(curr_largest_good_num):
                        curr_largest_good_num = good_num
        return curr_largest_good_num