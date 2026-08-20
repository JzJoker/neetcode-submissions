class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        listS.sort()
        listT.sort()
        return listS == listT