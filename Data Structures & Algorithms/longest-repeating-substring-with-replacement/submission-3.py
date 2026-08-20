class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # count repeated character
        count = defaultdict(int)

        l = 0
        maxf = 0
        for r in range(len(s)):
            # Count character
            count[s[r]] += 1
            # Set max correct character count
            maxf = max(maxf, count[s[r]])

            # While the # of characters minus the most common letter
            # is more than k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

        