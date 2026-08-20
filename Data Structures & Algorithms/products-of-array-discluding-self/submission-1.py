class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        z_count = 0
        for num in nums:
            if num == 0:
                z_count += 1
            else:
                product = product * num
            
        products = []
        if z_count > 1:
            products = [0] * len(nums)
            return products
        for num in nums:
            if z_count == 1:
                if num != 0:
                    products.append(0)
                else:
                    products.append(product)
            else:
                products.append(int(product / num))
        return products