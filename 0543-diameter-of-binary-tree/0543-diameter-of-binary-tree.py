# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        
        def bfs(root):
            if not root: return 0
            leftHeight = bfs(root.left)
            rightHeight = bfs(root.right)
            height = max(leftHeight, rightHeight) + 1
            diameter = leftHeight + rightHeight
            
            nonlocal res
            res = max(res, diameter)
            
            return height
        
        bfs(root)
        return res
