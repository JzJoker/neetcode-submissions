class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = float('inf')
        res = 0
        for price in prices[0::]:
            profit = price - prevMin
            res = max(res, profit)
            prevMin = min(prevMin, price)
        return res