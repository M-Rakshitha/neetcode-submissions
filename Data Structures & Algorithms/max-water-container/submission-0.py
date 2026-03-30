class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximun = 0 
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maximun = max(area, maximun)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maximun