class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prevMin = float('inf')
        for price in prices:
            res = max(res, price - prevMin)
            prevMin = min(prevMin, price)
        return res
