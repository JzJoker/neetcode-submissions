class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCharacters = [0] * 27
        tCharacters = [0] * 27
        start = ord('a')
        for i in range(len(s)):
            sCharacters[ord(s[i]) - start] += 1
            tCharacters[ord(t[i]) - start] += 1
        print(sCharacters)
        print(tCharacters)
        if sCharacters != tCharacters:
            return False
        return True