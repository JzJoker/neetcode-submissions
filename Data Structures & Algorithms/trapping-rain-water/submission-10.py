class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxLeft = max(height[l], maxLeft)
                res += maxLeft - height[l]
            elif height[r] <= height[l]:
                r -= 1
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]
        return res