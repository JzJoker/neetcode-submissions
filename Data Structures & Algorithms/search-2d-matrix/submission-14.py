class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        if not matrix:
            return False
        while l <= r:
            mid = ( l + r ) // 2
            if matrix[mid][0] > target:
                r = mid - 1

            elif matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    break
                l = mid + 1
            else:
                return True
        print(mid)
        a, b = 0, len(matrix[mid]) - 1
        while a <= b:
            mid1 = (a + b) // 2
            if matrix[mid][mid1] > target:
                b = mid1 - 1
            elif matrix[mid][mid1] < target:
                a = mid1 + 1
            else:
                return True
        return False


