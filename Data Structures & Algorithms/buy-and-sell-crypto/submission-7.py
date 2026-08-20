class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = float('inf')
        maxProf = 0
        for price in prices:
            prevMin = min(prevMin, price)
            maxProf = max(maxProf, price - prevMin)
        return maxProf
