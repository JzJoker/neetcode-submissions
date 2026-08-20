class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r -= 1
            elif matrix[mid][-1] < target:
                l += 1
            else:
                break
        if l > r:
            return False
        l1, r1 = 0, len(matrix[mid])    
        while l1 <= r1:
            mid1 = (l1 + r1) // 2
            num = matrix[mid][mid1]
            if num > target:
                r1 = mid1 - 1
            elif num < target:
                l1 = mid1 + 1
            else:
                return True
        return False