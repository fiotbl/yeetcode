# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        res = dummy = ListNode(0)
        dummy.next = head
        
        for _ in range(n):
            r = r.next
                
        while r:
            dummy = dummy.next
            r = r.next
        
        dummy.next = dummy.next.next
        
        return res.next