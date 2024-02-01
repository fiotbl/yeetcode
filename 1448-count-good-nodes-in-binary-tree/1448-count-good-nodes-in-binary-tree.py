# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        
        def dfs(root, currMax):
            if not root: return
            nonlocal total
            
            if root.val >= currMax: 
                total +=1
                currMax = root.val
            
            dfs(root.left, currMax)
            dfs(root.right, currMax)
        
        dfs(root, -10**5)
        
        return total
        
            
        
            