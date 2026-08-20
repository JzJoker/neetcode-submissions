class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new += s[i].lower()
        return new == new[::-1]
