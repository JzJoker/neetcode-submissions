class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(nums[l], nums[r])
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return mid
        return -1
            