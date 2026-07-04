class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = list(len(matrix[0]) * [0])
        for i in range(len(new_matrix)):
            for j in range(len(matrix)):
                if new_matrix[i] == 0:
                    new_matrix[i] = [0]
                else:
                    new_matrix[i] += [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix