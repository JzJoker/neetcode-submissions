class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag1 = diag2 = 0
        curRow = curCol = 0
        for i in range(len(mat)):
            if i != len(mat[0]) - i - 1:
                diag2 += mat[len(mat[0]) - i - 1][i]
            diag1 += mat[i][i]
            print(mat[i][i])
            print(mat[len(mat[0]) - i - 1][i])
        return diag1 + diag2
