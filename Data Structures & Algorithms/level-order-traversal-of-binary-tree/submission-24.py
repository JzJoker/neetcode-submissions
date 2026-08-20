# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            dfs(root.left, depth + 1)
            res[depth].append(root.val)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res