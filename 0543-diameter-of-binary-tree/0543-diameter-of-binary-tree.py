# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            if not root: return 0 # return 0 for height if there is no node
            left, right = dfs(root.left), dfs(root.right) # get height of left and right subtrees
            diameter = left + right # diameter will be height of left node plus height of right node 
             
            nonlocal res
            res = max(res, diameter) # update res if curr diameter more than curr res
            
            return 1 + max(left, right) # return the curr height of node
        
        dfs(root)
        return res