# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(n):
            if not n: return 0
            left, right = dfs(n.left), dfs(n.right)
            height = max(left, right) + 1
            
            nonlocal res 
            if left+right > res:
                res = left+right
            return height
                
        dfs(root)
        return res