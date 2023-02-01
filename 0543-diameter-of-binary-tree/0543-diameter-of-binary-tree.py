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
            if not root: return -1 # return -1 for height if there is no node
            left, right = dfs(root.left), dfs(root.right) # get height of left and right subtrees
            diameter = 2 + left + right # diameter will be height of left node plus height of right node plus 2 for the 2 edge that connects from node to left and right
             
            nonlocal res
            res = max(res, diameter) # update res if curr diameter more than curr res
            
            return 1 + max(left, right)
        
        dfs(root)
        return res