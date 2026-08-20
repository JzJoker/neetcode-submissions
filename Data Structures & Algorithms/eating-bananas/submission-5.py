class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            time = 0
            k = (r + l) // 2
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res