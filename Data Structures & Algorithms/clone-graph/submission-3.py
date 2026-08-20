"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def dfs(start):
            if start in clones:
                return clones[start]
            clone = Node(start.val)
            clones[start] = clone
            for nei in start.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return None if not node else dfs(node)