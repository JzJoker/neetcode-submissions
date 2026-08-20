# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            rightMax = max(dfs(node.right), 0)
            leftMax = max(dfs(node.left), 0)

            res = max(res, rightMax + node.val + leftMax)
            return node.val + max(rightMax, leftMax)
        dfs(root)
        return res