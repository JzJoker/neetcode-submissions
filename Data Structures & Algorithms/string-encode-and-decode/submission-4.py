class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        count = fch = 0
        res = []
        while count < len(s):
            while s[fch] != '#':
                fch += 1
            count = int(s[count:fch])
            res.append(s[fch + 1:fch + count + 1])
            fch += count + 2
            count = fch - 1
        return res


            