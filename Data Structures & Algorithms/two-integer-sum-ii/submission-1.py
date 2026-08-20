class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numIndex = {}
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in numIndex:
                return [numIndex[compliment] + 1, i + 1]
            numIndex[numbers[i]] = i
        return []