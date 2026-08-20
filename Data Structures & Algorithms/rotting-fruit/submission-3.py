class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
                    fresh -= 1
                    minutes = max(minutes, grid[r][c] - 1)
        return -1 if fresh else minutes
