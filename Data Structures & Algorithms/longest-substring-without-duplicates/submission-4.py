class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = cnt = 0
        seen = set()
        seen.add(s[0])
        l, r = 0, 1
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            res = max(res, len(seen))
            r += 1
        return res