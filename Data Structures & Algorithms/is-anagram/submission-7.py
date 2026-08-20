class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = [0] * 27
        countT = [0] * 27
        for i in range(len(s)):
            countS[ord(s[i]) - ord('a')] += 1
            countT[ord(t[i]) - ord('a')] += 1
        return countS == countT