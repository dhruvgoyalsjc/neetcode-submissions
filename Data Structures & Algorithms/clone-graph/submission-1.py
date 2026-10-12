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

        ogToCopy = {}

        def dfs(root: Optional['Node']):
            if root in ogToCopy:
                return ogToCopy[root]

            rootCopy = Node(root.val)
            ogToCopy[root] = rootCopy

            for neighbor in root.neighbors:
                rootCopy.neighbors.append(dfs(neighbor))
            
            return rootCopy
        
        return dfs(node)
            