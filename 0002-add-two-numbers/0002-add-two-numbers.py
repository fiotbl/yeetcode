# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = ""
        val2 = ""
        dummy = ListNode()
        cur = dummy
        
        while l1:
            val1 = str(l1.val) + val1
            l1 = l1.next
        
        while l2:
            val2 = str(l2.val) + val2
            l2 = l2.next
            
        total = str(int(val1) + int(val2))
        for i in range(len(total)-1, -1, -1):
            cur.next = ListNode(total[i])
            cur = cur.next
        
        return dummy.next