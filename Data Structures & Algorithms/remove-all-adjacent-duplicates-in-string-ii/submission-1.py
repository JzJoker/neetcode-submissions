class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l =  0
        r = 1
        def recurse(l, r, s):
            while r < len(s):
                if s[r] != s[l]:
                    count = 0
                    l = r
                if r - l  + 1== k:
                    s = s[0:l] + s[r + 1::]
                    return recurse(0,1, s)
                r += 1
            return s
        return recurse(l, r, s)