class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()
                for rd, cd in directions:
                    nr, nc = rd + r, cd + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count