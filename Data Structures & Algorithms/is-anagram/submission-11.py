class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = defaultdict(int)
        tCount = defaultdict(int)
        for i in range(len(t)):
            sCount[s[i]] += 1
            tCount[t[i]] += 1
        return sCount == tCount