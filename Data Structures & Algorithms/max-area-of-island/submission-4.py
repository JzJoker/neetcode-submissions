class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        maxf = 0
        
        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        area += 1
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxf = max(bfs(r, c), maxf)
        return maxf