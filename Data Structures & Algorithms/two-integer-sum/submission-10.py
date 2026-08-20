class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(list)
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if len(seen[compliment]) > 0:
                return [seen[compliment][0], i]
            seen[num].append(i)