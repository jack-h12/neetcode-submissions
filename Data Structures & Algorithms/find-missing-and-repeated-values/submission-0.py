class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums_set = set()
        output = [0, 0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in nums_set:
                    output[0] = grid[i][j]
                else:
                    nums_set.add(grid[i][j])
        
        for i in range(len(grid) * len(grid)):
            if i + 1 not in nums_set:
                output[1] = i + 1
                break
        
        return output
