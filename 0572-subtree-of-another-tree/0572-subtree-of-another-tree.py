# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equals(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val: return False
            return equals(root.left, subroot.left) and equals(root.right, subroot.right)
            
        
        def dfs(root, subroot):
            if not root: return False
            if equals(root, subroot): return True
            
            left = dfs(root.left, subroot)
            right = dfs(root.right, subroot)
            return left or right
        
        return dfs(root, subRoot)