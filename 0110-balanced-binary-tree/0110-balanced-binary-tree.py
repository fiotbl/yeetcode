# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node: return [True, 0]
            
            left, right = balanced(node.left), balanced(node.right)
            isNodeBalanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            
            return [isNodeBalanced, max(left[1], right[1]) + 1]
        
        
        return balanced(root)[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def balancedDfs(node):
#             if not node: return [True, 0]
            
#             left, right = balancedDfs(node.left), balancedDfs(node.right)
            
#             balanced = (left[0] and right[0] and abs(left[1]-right[1])<=1)
                
#             return [balanced, max(left[1], right[1]) + 1]
                
        
#         return balancedDfs(root)[0]