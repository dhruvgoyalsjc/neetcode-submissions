# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderRec(node, k):
            if not node:
                return None, k

            # Search left
            val, k = inOrderRec(node.left, k)
            if val is not None:
                return val, k

            # Visit current
            k -= 1
            if k == 0:
                return node.val, k

            # Search right
            return inOrderRec(node.right, k)

        val, _ = inOrderRec(root, k)
        return val