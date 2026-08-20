class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            for i in seen:
                if i == num:
                    return True
            seen.append(num)
        return False