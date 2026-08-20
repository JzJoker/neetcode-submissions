class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, d1 = defaultdict(int), defaultdict(int)
        for ch in t:
            d1[ch] += 1
        l = have = 0
        need = len(d1)
        res, reslen = [-1, -1], float('inf')
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            if ch in d1 and window[ch] == d1[ch]:
                have += 1
                while have == need:
                    if r - l + 1 < reslen:
                        res = [l, r]
                        reslen = min(reslen, r - l + 1)
                    window[s[l]] -= 1
                    if s[l] in d1 and window[s[l]] < d1[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l: r + 1] if not reslen == float('inf') else ""

                