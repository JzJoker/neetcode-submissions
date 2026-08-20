class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = float('inf')
        maxProf = 0
        for price in prices:
            maxProf = max(maxProf, price - prevMin)
            prevMin = min(prevMin, price)
        return maxProf
