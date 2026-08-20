class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = {'?', '.', '!', ';', ':', ' ', '\'', ' ', ','}
        l, r = 0, len(s) - 1
        while l < r:
            while s[l] in punc and l < r:
                l += 1
            while s[r] in punc and r > l:
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True