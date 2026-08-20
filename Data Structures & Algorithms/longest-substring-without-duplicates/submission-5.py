class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        l = 0 

        for r, char in enumerate(s):
            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char] + 1
            last_seen[char] = r
            max_len = max(max_len, r - l + 1)

        return max_len
