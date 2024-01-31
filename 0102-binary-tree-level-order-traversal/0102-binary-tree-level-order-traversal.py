# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = []
        if root: stack.append(root)
        
        while stack:
            length = len(stack)
            ans = []
            for _ in range(length):
                curr = stack.pop(0)
                if curr:
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
                    ans.append(curr.val)
            res.append(ans)
        
        return res