class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        seen = defaultdict(int)
        for ch in s1:
            d1[ch] += 1
        have, need = 0, len(d1)
        l = 0
        count = 0
        for r in range(len(s2)):
            ch = s2[r]
            seen[ch] += 1
            count += 1
            if ch in d1 and d1[ch] == seen[ch]:
                have += 1
                if have == need:
                    return True
            if count == len(s1):
                left = s2[l]
                if left in d1 and seen[left] == d1[left]:
                    have -=1
                seen[left] -= 1
                l += 1
                count -= 1
        return False
