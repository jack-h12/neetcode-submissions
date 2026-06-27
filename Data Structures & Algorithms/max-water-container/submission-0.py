class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            if curr_area > curr_max:
                curr_max = curr_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return curr_max
