class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        if not matrix:
            return False
        t, b = 0, len(matrix) - 1
        i = 0
        while t <= b:
            i = (b + t) // 2
            print(matrix[i])
            if target > matrix[i][w - 1]:
                t = i + 1
            elif target < matrix[i][0]:
                b = i - 1
            else:
                break
        if not (t <= b):
            return False
        row = (t + b) // 2
        l, r = 0, w
        while l <= r:
            m = (l + r) // 2
            if target < matrix[i][m]:
                r = m - 1
            elif target > matrix[i][m]:
                l = m + 1
            else:
                return True
        return False