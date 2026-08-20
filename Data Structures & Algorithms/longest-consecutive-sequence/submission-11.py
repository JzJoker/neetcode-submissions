class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        numsSet = set(nums)
        for num in numsSet:
            if num - 1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1
                streak = max(streak, length)
        return streak   