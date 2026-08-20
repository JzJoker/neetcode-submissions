class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, dict1 = defaultdict(int), defaultdict(int)
        for ch in s1:
            dict1[ch] += 1
        have, need = 0, len(dict1)
        count = 0
        l = 0
        for i in range(len(s2)):
            ch = s2[i]
            window[ch] += 1
            print(list(window.keys()))
            count += 1
            if ch in dict1 and window[ch] == dict1[ch]:
                have += 1
                if have == need:
                    print(have, need)
                    return True
            if count == len(s1):
                left = s2[l]
                if left in dict1 and window[left] == dict1[left]:
                    have -= 1          # it was matched, now it won't be
                window[left] -= 1
                l += 1
                count -= 1
            print(have, need)
            
        return False
