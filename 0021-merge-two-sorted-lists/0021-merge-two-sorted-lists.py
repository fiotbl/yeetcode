# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = currHead = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                currHead.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                currHead.next = list2
                list2 = list2.next
            currHead = currHead.next
            
        if list1:
            currHead.next = list1
        
        if list2:
            currHead.next = list2
        
        return ansHead.next
                   
                  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ansHead = movingHead = ListNode()
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 movingHead.next= list1
#                 list1 = list1.next
#             elif list1.val > list2.val:
#                 movingHead.next= list2
#                 list2 = list2.next
#             movingHead = movingHead.next
        
#         if list1:
#             movingHead.next = list1
            
#         if list2:
#             movingHead.next = list2
        
#         return ansHead.next
                  
                