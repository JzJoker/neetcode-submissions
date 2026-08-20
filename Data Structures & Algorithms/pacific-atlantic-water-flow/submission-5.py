class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        
        def bfs(start):
            seen = set(start)
            q = deque(start)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            return seen
    
        pac = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        return [list(cell) for cell in bfs(pac) & bfs(atl)]