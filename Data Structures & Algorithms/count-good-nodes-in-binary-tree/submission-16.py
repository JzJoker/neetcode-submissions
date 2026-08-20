# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, prevMax):
            nonlocal res
            if not node:
                return 
            print(prevMax, node.val)
            if node.val >= prevMax:
                res += 1
            dfs(node.left, max(prevMax, node.val))
            dfs(node.right, max(prevMax, node.val))
        dfs(root, float('-inf'))
        return res
            