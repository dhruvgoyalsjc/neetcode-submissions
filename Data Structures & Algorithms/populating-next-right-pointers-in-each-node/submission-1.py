"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        def bfs(root: 'Optional[Node]'):
            q = deque([root])
            layer = []

            while q:
                curr = q.popleft()

                if curr.left:
                    layer.append(curr.left)
                if curr.right:
                    layer.append(curr.right)
                
                if q:
                    curr.next = q[0]
                else:
                    q.extend(layer)
                    layer = []
            
            return root
        
        return bfs(root)