class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        pair = {')':'(', '}':'{',']':'['}
        for ch in s:
            print(stack)
            if ch not in pair.values():
                print(pair[ch])
                if not stack or pair[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True