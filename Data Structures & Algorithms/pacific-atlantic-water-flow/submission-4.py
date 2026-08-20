class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(heights), len(heights[0])

        def bfs(cell):
            seen = set(cell)
            q = deque(cell)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        pac = [(r,0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        return [list(cell) for cell in bfs(pac) & bfs(atl)]