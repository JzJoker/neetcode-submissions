class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        res = []
        for anagramList in anagrams.values():
            res.append(anagramList)
        return res