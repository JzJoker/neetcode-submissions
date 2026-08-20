class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zCount = 0
        prod = 1
        for num in nums:
            if num == 0:
                zCount += 1
                if zCount > 1:
                    return [0 for i in range(len(nums))]
            else:
                prod *= num
        res = []
        for num in nums:
            if zCount == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // num)
        return res