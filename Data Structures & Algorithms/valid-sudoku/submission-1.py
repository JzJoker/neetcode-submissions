class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subboxes = defaultdict(set)
        for irow in range(len(board)):
            for icol in range(len(board[irow])):
                num = board[irow][icol]
                if num != ".":
                    box = (irow // 3) * 3 + (icol // 3) + 1
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