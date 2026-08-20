from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(starts):
            seen = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        pacific = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        return [list(cell) for cell in bfs(pacific) & bfs(atlantic)]