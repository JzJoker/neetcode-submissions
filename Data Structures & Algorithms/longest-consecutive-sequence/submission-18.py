class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                cnt = 1
                while num + cnt in numsSet:
                    cnt += 1
                res = max(res, cnt)
        return res