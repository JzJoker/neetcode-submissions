class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen = set()
            seen.add((r, c))
            escape = False
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 'O' and (nr, nc) not in seen:
                            q.append((nr, nc))
                            seen.add((nr, nc))
                    else:
                        escape = True
            if not escape:
                for r, c in seen:
                    board[r][c] = 'X'
                return

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    bfs(r, c)