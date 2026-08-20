class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxp = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxp = max(profit, maxp)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxp