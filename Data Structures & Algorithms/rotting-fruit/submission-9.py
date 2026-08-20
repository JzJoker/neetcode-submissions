class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        minutes = -1
        fresh = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if not fresh:
            return 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] + 1
                    minutes = max(minutes, grid[nr][nc] - 2)
                    q.append((nr, nc))
                    fresh -= 1
        
        return -1 if fresh else minutes