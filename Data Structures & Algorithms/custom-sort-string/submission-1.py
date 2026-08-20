class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        s = list(s)
        for ch in order:
            print('adding', ch + "'s")
            i = 0
            while i < len(s):
                c = s[i]
                if c == ch:
                    s.pop(i)
                    print(s)
                    res += str(c)
                    print('added', c)
                    print(res)
                    i -= 1
                i += 1
        for ch in s:
            res += str(ch)
        return res