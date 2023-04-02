# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = []
        cur = root
        m = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            m += 1
            cur = stack.pop()
            if m == k: return cur.val
            res.append(cur.val)
            cur = cur.right
        print(res)
            