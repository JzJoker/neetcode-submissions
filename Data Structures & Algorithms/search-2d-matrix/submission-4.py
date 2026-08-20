class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        l, r = 0, len(matrix[0]) - 1
        i = 0
        while i < len(matrix) and not matrix[i][l] <= target <= matrix[i][r]:
            i += 1
        if i >= len(matrix):
            return False
        while l <= r:
            mid = (r + l)//2
            if matrix[i][mid] > target:
                r = mid - 1
            elif matrix[i][mid] < target:
                l = mid + 1
            else:
                return True
        return False