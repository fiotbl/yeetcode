# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            depth = max(left, right)
            return 1+depth
        
        return dfs(root)