class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            if target - nums[i] in compliments:
                return [compliments[target-nums[i]], i]
            compliments[nums[i]] = i