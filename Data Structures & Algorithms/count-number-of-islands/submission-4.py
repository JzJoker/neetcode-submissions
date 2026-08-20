class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[1, 0],[-1, 0],[0, 1],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            grid[r][c] = "0"
            q = deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(rows) and c in range(cols)
                        and grid[r][c] == "1"):
                        grid[r][c] = "0"
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands