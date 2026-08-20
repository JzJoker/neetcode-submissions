class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == '+':
                stack.append(stack.pop(-2) + int(stack.pop()))
            elif token == '-':
                stack.append(stack.pop(-2) - int(stack.pop()))
            elif token == '*':
                stack.append(stack.pop(-2) * int(stack.pop()))
            elif token == '/':
                stack.append(int(stack.pop(-2) / int(stack.pop())))

            else:
                stack.append(int(token))
        return int(stack[0])