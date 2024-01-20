# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
            
        curr = head      
        while curr and prev:
            tmp = curr.next
            tmp2 = prev.next
            curr.next = prev
            prev.next = tmp
            prev = tmp2
            curr = tmp
            
            
            
            
            
            