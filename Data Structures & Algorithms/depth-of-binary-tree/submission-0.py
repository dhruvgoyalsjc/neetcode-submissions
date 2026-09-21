# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def maxDepthRec(root):
            if not root:
                return 0
            maxDepth = 1 + max(maxDepthRec(root.left), maxDepthRec(root.right))
            return maxDepth

        return maxDepthRec(root)