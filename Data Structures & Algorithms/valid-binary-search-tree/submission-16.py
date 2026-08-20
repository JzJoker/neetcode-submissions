# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minf, maxf):
            if not node:
                return True
            if node.val <= minf or node.val >= maxf:
                return False
            return dfs(node.left, minf, node.val) and dfs(node.right, node.val, maxf)
        return dfs(root, float('-inf'), float('inf'))