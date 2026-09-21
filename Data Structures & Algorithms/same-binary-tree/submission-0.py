# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q # True if both are None
        
        if not q:
            return False # False if p exists but q is None

        # now we know for sure both nodes exist
        if q.val != p.val:
            return False
        
        return (self.isSameTree(p.left, q.left) 
            and self.isSameTree(p.right, q.right))