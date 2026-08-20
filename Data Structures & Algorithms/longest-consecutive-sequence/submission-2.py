class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        curCnt = maxCnt = 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curCnt += 1
                maxCnt = max(maxCnt, curCnt + 1)
            else:
                curCnt = 0
        return maxCnt