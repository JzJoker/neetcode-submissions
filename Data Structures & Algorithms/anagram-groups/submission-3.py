class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            groups[str(sorted(st))].append(st)
        return list(groups.values())