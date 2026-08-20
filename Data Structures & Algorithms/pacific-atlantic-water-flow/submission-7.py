class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        def bfs(start):
            q = deque(start)
            seen = set(start)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            return seen
        
        pac = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atl = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        
        return [list(cell) for cell in bfs(pac) & bfs(atl)]
