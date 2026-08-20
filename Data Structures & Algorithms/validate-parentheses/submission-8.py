class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {'{' : '}', '[' :']', '(' : ')'}
        for ch in s:
            if ch in openings:
                stack.append(ch)
            elif len(stack) == 0 or ch != openings[stack.pop(-1)]:
                return False
        return len(stack) == 0