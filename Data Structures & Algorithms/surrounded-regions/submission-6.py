class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            q = deque([(r, c)])
            board[r][c] = "S"
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        q.append((nr, nc))

        border = ([(0, c) for c in range(cols)]                    
        + [(rows - 1, c) for c in range(cols)]           
        + [(r, 0) for r in range(1, rows - 1)]            
        + [(r, cols - 1) for r in range(1, rows - 1)])

        for r, c in border:
            if board[r][c] == "O":
                bfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
