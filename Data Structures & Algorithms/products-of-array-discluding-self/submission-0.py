class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zCnt = 0
        for num in nums:
            if num != 0:
                product = product * num
            else:
                zCnt += 1
        if zCnt > 1:
            return [0] * len(nums) 
        elif zCnt == 1:
            products = []
            for num in nums:
                if num == 0:
                    products.append(product)
                else:
                    products.append(0)
        else:
            products = []
            for num in nums:
                products.append(product//num)
        return products
