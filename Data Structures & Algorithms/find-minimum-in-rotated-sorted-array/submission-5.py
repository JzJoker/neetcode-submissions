class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = 0
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r] or len(nums) == 1:
            return nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
            elif nums[m] <= nums[r]:
                r = m
            if nums[m] > nums[m + 1]:
                break
        res = nums[m+1]
        return res

