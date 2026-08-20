class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            Chcounts = [0] * 26
            for ch in s:
                Chcounts[ord(ch) - ord('a')] += 1
            counts[tuple(Chcounts)].append(s)
        return list(counts.values())