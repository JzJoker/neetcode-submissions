class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tcounts = [0] * 27
        scounts = [0] * 27
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            tcounts[ord(t[i]) - ord('a')] += 1
            scounts[ord(s[i]) - ord('a')] += 1
        return tcounts == scounts
 