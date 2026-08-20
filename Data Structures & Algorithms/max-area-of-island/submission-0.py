class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == 1):
                        area += 1
                        q.append((r, c))
                        grid[r][c] = 0
            return area
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res