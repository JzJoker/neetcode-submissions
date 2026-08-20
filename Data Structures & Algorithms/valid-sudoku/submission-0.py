class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subboxes = defaultdict(set)
        # box 1 - 0 <= icol <=2, 0 <= irow <= 2
        # box 2 - 3 <= icol <=5, 0 <= irow <= 2
        # box 3 - 6 <= icol <=8, 0 <= irow <= 2
        # box 4 - 0 <= icol <=2, 3 <= irow <= 5
        # box 5 - 3 <= icol <=5, 3 <= irow <= 5
        # box 6 - 6 <= icol <=8, 3 <= irow <= 5
        # box 7 - 0 <= icol <=2, 6 <= irow <= 8
        # box 8 - 3 <= icol <=5, 6 <= irow <= 8
        # box 9 - 6 <= icol <=8, 6 <= irow <= 8
        for irow in range(len(board)):
            for icol in range(len(board[irow])):
                num = board[irow][icol]
                if num != ".":
                    if 0 <= icol and icol <=2 and 0 <= irow and irow <= 2:
                        box = 1
                    elif 3 <= icol and icol <=5 and 0 <= irow and irow <= 2:
                        box = 2
                    elif 6 <= icol and icol <=8 and 0 <= irow and irow <= 2:
                        box = 3
                    elif 0 <= icol and icol <=2 and 3 <= irow and irow <= 5:
                        box = 4
                    elif 3 <= icol and icol <=5 and 3 <= irow and irow <= 5:
                        box = 5
                    elif 6 <= icol and icol <=8 and 3 <= irow and irow <= 5:
                        box = 6
                    elif 0 <= icol and icol <=2 and 6 <= irow and irow <= 8:
                        box = 7
                    elif 3 <= icol and icol <=5 and 6 <= irow and irow <= 8:
                        box = 8
                    elif 6 <= icol and icol <=8 and 6 <= irow and irow <= 8:
                        box = 9  
                    if num in rows[irow]:
                        return False
                    if num in columns[icol]:
                        return False
                    if num in subboxes[box]:
                        return False
                    rows[irow].add(num)
                    columns[icol].add(num)
                    subboxes[box].add(num)
        return True