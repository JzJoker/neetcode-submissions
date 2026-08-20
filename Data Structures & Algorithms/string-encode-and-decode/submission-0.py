class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "**here**"
        return res
    def decode(self, s: str) -> List[str]:
        s = s.split("**here**")
        if s[-1] == "":
            return s[:-1]
        return s