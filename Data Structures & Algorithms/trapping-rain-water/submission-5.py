class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        water = 0
        while r != len(height):
            if height[l] <= height[r]:
                water += (r - l - 1) * height[l]
                # print((r - l - 1), "x", height[l], "added", (r - l - 1) * height[l], "water")
                l += 1
                while l != r:
                    water -= height[l]
                    # print("removed", height[l], "water")
                    l += 1
            r += 1
            if r == len(height) and l != len(height) - 1:
                # if end is reached, store max height and index after l
                r = l + 1
                rmaxIndex = r
                rmax = height[r]
                while r != len(height):
                    rmax = max(height[r], rmax)
                    if rmax == height[r]:
                        rmaxIndex = r
                    r += 1
                # print("max height:", rmax, "max index:", rmaxIndex)
                water += rmax * (rmaxIndex - l - 1)
                # print((rmaxIndex - l - 1), "x", rmax, "added", rmax * (rmaxIndex - l - 1), "water")
                l += 1
                while l != rmaxIndex:
                    water -= height[l]
                    # print("removed", height[l], "water")
                    l += 1
                l = rmaxIndex
                r = l + 1
            # print(l, r)
        return water