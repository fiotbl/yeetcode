# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root] if root else []
        res =[]
        
        while queue:
            tmp = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                tmp.append(curr.val)
            res.append(tmp)
            
        return res
        