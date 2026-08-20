class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = res = 0
        for r in range(len(s)):
            ch = s[r]
            while ch in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(ch)
        return res