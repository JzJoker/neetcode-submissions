class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 27
        totalChars = 0
        left = 0
        maj = 0
        res = 0
        for ch in s:
            i = ord(ch) - ord('A')
            counts[i] += 1
            totalChars += 1
            if counts[i] > maj:
                maj = counts[i]
            while totalChars - maj > k:
                j = ord(s[left]) - ord('A')
                counts[j] -= 1
                totalChars -= 1
                left += 1
            res = max(res, totalChars)
        return res