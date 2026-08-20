class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        seen = set()
        res = 0
        for ch in s:
            window.append(ch)
            print(window)
            while ch in seen:
                seen.remove(window.pop(0))
            res = max(res, len(window))
            seen.add(ch)
        return res
        