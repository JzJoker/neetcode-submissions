class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMin = prices[0]
        maxP = 0
        for price in prices:
            profit = price - preMin
            maxP = max(profit, maxP)
            preMin = min(preMin, price)
        return maxP