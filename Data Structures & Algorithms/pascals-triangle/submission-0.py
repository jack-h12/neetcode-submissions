class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output_list = []
        for i in range(numRows):
            output_list.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    output_list[i].append(1)
                else:
                    output_list[i].append(output_list[i-1][j-1] + output_list[i-1][j])
        return output_list