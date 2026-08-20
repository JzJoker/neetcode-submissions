class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            rows, cols = len(grid), len(grid[0])
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1:
                return
            nonlocal visit
            land = grid[r][c]
            if land == "0" or tuple([r,c]) in visit:
                return
            visit.add(tuple([r, c]))
            bfs(r - 1, c)
            bfs(r + 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                land = grid[r][c]
                if land == "0" or tuple([r, c]) in visit:
                    continue
                islands += 1
                bfs(r, c)
        return islands

        