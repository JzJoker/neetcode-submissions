class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        enum = list(enumerate(nums))
        sortedNums = sorted(enum, key=lambda x: x[1])
        while left <= right:
            tot = sortedNums[left][1] + sortedNums[right][1]
            print(tot)
            if tot == target:
                return sorted([sortedNums[left][0],sortedNums[right][0]])
            elif tot > target:
                right -= 1
            else:
                left += 1
        return [0,0]

        