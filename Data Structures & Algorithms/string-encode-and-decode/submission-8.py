class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[(l) : r ])
            l = r
            r += length + 1
            res.append(s[l + 1 : r])
            l = r
        return res