class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for key in counts.keys():
            if counts[key] == 1:
                return key