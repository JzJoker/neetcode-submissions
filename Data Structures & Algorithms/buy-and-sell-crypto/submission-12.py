class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = prices[0]
        res = 0
        for price in prices:
            profit = price - prevMin
            res = max(res, profit)
            prevMin = min(price, prevMin)
        return res