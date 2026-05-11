"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}
        def cloneNode(node):
            if not node:
                return None
            clone = Node(node.val, [])
            copies[clone.val] = clone
            for neighbor in node.neighbors:
                if neighbor.val in copies:
                    clone.neighbors.append(copies[neighbor.val])
                else:
                    clone.neighbors.append(cloneNode(neighbor))
            return clone
        return cloneNode(node)