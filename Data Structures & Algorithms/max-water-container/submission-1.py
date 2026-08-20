class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        res = 0
        while l < r:
            water = min(heights[r], heights[l]) * (r - l)
            res = max(res, water)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res