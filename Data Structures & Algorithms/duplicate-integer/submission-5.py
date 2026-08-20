class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(self.CustomSet(nums)) == len(nums)

    def CustomSet(self, nums) -> list:
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
        return res