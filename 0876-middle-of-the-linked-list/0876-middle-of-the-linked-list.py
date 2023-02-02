# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        
        while head:
            count += 1
            head = head.next

        for i in range(count//2):
            curr = curr.next
            pass
        return curr