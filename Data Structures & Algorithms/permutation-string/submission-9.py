class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1counts = [0] * 27
        counts = [0] * 27
        left = 0
        size = 0
        matches = 0
        required = 0
        for i in range(len(s1)):
            if counts[ord(s1[i]) - ord('a')] == 0:
                required += 1
            counts[ord(s1[i]) - ord('a')] += 1


        for i in range(len(s2)):
            print(matches)
            s1counts[ord(s2[i]) - ord('a')] += 1
            size += 1
            if size > len(s1):
                if counts[ord(s2[left]) - ord('a')] == s1counts[ord(s2[left]) - ord('a')]:
                    matches -= 1
                s1counts[ord(s2[left]) - ord('a')] -= 1
                left += 1
                size -= 1
            if counts[ord(s2[i]) - ord('a')] == s1counts[ord(s2[i]) - ord('a')]:
                matches += 1
                if matches == required:
                    return True
            
        return False
