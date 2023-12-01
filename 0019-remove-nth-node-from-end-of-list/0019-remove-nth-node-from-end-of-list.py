# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1
        
        curr = head
        i = 0
        prev = None
        
        if count - n == 0:
            return curr.next
        
        while curr:
            if i == (count - n):
                prev.next = curr.next
                break
            else:
                prev = curr
                curr = curr.next
                i += 1
        
        return head