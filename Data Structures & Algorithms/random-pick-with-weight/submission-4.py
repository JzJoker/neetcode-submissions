import random

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        cur = 0
        for num in w:
            cur += num
            self.prefix.append(cur)
        self.total = cur

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid          # keep mid as a candidate, don't skip past it
        return l