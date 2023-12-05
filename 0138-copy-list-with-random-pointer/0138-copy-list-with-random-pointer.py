"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copy = {None:None}
        
        while curr:
            copied = Node(curr.val)
            copy[curr] = copied
            curr = curr.next
        curr = head
        
        while curr:
            tmp = copy[curr]
            print(tmp)
            tmp.next = copy[curr.next]
            tmp.random = copy[curr.random]
            curr = curr.next
        
        return copy[head]
            