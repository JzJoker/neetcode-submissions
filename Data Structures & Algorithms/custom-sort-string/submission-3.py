class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        res = ""
        for ch in s:
            freq[ch] += 1
        for ch in order:
            res += ch * freq[ch]
            freq.pop(ch)
        for ch in freq.keys():
            res += ch * freq[ch]
        return res