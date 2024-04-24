"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = []
        nodeMap = {}
        
        if not node: return
        
        nodeMap[node] = Node(node.val)
        queue.append(node)
        
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                nodeMap[n].neighbors.append(nodeMap[neighbor])
        return nodeMap[node]