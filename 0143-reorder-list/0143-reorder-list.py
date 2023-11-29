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
        # first find the middle using slow and fast
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # next reverse second linked list
        curr = slow.next
        prev = slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # merge two linked 
        first, snd = head, prev
        while snd:
            tmp = first.next
            tmp2 = snd.next
            first.next = snd 
            snd.next = tmp
            first, snd = tmp, tmp2
            
        
        
        