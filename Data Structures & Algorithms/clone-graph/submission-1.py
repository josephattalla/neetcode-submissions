"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def cloneNode(node):
            print(node.val)
            if node.val in visited:
                return visited[node.val]
            
            visited[node.val] = Node(node.val, [])

            for neighbor in node.neighbors:
                visited[node.val].neighbors.append(cloneNode(neighbor))
            
            return visited[node.val]

        return cloneNode(node)