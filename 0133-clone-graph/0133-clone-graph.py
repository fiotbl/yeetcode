"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visitedNodes = {}
        
        def clone(node):
            if not node: return
            if node in visitedNodes:
                return visitedNodes[node]
            
            copy = Node(node.val)
            visitedNodes[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
                
            return copy
                
        return clone(node)