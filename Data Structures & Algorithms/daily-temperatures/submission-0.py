class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            temp = temperatures[i]
            if stack:
                j = len(stack) - 1
                while j >= 0:
                    day = stack[j]
                    if temp > day[0]:
                        res[day[1]] = i - day[1]
                        stack.pop(j)
                    j -= 1
            stack.append([temp, i])
            i += 1
        return res


