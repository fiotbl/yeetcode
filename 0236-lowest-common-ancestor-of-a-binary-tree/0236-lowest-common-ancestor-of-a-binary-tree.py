# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if not root: return
            if root == p or root == q: 
                return root
            
            left, right = dfs(root.left), dfs(root.right)
            if not left and not right: return
            
            if left and right: return root
            
            return left if left else right
        
        return dfs(root)
            