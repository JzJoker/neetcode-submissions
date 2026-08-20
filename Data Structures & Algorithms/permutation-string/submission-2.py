class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = defaultdict(int)
        for ch in s1:
            dict1[ch] += 1
        
        dict2 = defaultdict(int)
        for ch in s2[:len(s1)]:
            dict2[ch] += 1    
            if dict1 == dict2:
                return True    
        l = 0
        for r in range(len(s1),len(s2)):
            dict2[s2[l]] -= 1
            if(dict2[s2[l]] == 0):
                del dict2[s2[l]]
            dict2[s2[r]] += 1
            if dict1 == dict2:
                return True
            l, r = l + 1, r + 1
        return False            