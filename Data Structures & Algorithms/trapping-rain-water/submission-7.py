class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        water = 0
        while l < r:
            if maxl <= maxr:
                water += max(0, maxl - height[l])
                l += 1
                maxl = max(maxl, height[l])
            else:
                water += max(0, maxr - height[r])
                r -= 1
                maxr = max(maxr, height[r])
            
        return water
