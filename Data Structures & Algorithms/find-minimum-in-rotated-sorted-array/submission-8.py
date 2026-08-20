class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = (l + r) // 2
            print(nums[mid])
            # Left half
            if nums[mid] >= nums[r]:
                l = mid + 1
            # Right half
            else:
                r = mid - 1
            res = min(res, nums[mid])

        return res
