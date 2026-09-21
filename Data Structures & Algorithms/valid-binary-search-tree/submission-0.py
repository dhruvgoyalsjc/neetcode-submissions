# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not (self.isValidBST(root.left) and self.isValidBST(root.right)):
            return False
        if root.left and self.getMax(root.left) >= root.val:
            return False
        if root.right and self.getMin(root.right) <= root.val:
            return False
        
        return True
    
    def getMax(self, root: Optional[TreeNode]) -> int:
            while (root.right):
                root = root.right
            return root.val

    def getMin(self, root: Optional[TreeNode]) -> int:
        while (root.left):
            root = root.left
        return root.val