# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            if not root: return 0
            left, right = bfs(root.left), bfs(root.right)
            
            return max(left, right) + 1
        
        return bfs(root)