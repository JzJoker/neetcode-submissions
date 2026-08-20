class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        res = 0
        for i in range(len(s)):
            ch = s[i]
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            res = max(res, i - left + 1)
        return res
        
