class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            width = 1
            currHeight = heights[i]
            l = i - 1
            r = i + 1
            while l >= 0:
                if heights[l] >= currHeight:
                    width += 1
                else:
                    break
                l -= 1
            while r < len(heights):
                if heights[r] >= currHeight:
                    width += 1
                else:
                    break
                r += 1
            area = width * currHeight
            largest = max(largest, area)
        return largest