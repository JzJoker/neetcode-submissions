class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            tot = 0
            for pile in piles:
                tot += math.ceil(pile / k)
            if tot > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res