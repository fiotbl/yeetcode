# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def search(root, leftLimit, rightLimit):
            if not root: return True
            
            if root.val <= leftLimit or root.val >= rightLimit: return False
            
            return search(root.left, leftLimit, root.val) and search(root.right, root.val, rightLimit)
        
        return search(root, -10**99, 10**99)
            
            