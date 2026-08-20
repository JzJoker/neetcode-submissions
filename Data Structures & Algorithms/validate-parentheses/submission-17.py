class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{':'}', '[':']', '(':')'}
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if brackets[stack.pop()] != ch:
                    return False
        if stack:
            return False
        return True