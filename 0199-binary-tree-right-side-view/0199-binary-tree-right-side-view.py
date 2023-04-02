# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]
                  
        while any(queue):
            qLen = len(queue)
            rightNode = None
            for i in range(qLen):
                node = queue.pop(0)
                if node:
                    rightNode = node
                    queue.append(rightNode.left)
                    queue.append(rightNode.right)
            res.append(rightNode.val)
            
        return res            
            
                
            