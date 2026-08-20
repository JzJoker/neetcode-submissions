class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = [0] * 27
        tCount = [0] * 27

        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1
        
        for i in range(len(sCount)):
            if sCount[i] != tCount[i]:
                return False
        return True