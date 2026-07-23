class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            curr_row_index = (l + r) // 2
            if matrix[curr_row_index][0] == target:
                return True
            elif matrix[curr_row_index][0] < target:
                for num in matrix[curr_row_index]:
                    if num == target:
                        return True
                l = curr_row_index + 1
            else: # if the first value in row is greater than target
                curr_row_index -= 1
                for num in matrix[curr_row_index]:
                    if num == target:
                        return True
                r = curr_row_index
        return False