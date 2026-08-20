class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, window = defaultdict(int), defaultdict(int)
        for ch in s1:
            d1[ch] += 1
        have = l = 0
        need = len(d1)
        count = 0
        for r in range(len(s2)):
            ch = s2[r]
            window[ch] += 1
            count += 1
            if ch in d1 and window[ch] == d1[ch]:
                have += 1
                if have == need:
                    return True
            if count == len(s1):
                left = s2[l]
                if left in d1 and d1[left] == window[left]:
                    have -= 1
                window[left] -= 1
                l += 1
                count -= 1
        return False
