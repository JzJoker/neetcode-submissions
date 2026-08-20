class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = [0] * 27
        left = 0
        size = 0
        s1counts = [0] * 27

        for i in range(len(s1)):
            counts[ord(s1[i]) - ord('a')] += 1
        print(counts)
        for i in range(len(s2)):

            s1counts[ord(s2[i]) - ord('a')] += 1
            size += 1
            if size > len(s1):
                s1counts[ord(s2[left]) - ord('a')] -= 1
                left += 1
                size -= 1
            if s1counts == counts:
                return True
            print(s1counts)
        return False
