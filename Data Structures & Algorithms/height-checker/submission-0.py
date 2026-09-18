class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        out_of_order = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                out_of_order += 1
        return out_of_order