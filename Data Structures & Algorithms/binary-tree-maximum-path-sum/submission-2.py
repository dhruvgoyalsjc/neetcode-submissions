# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        # should return the max if we DON'T split on root
        def getMaxRecursive(root) -> int:
            nonlocal res

            if not root:
                return 0

            # fig out max sum if we do split on root
            maxLeft = max(0, getMaxRecursive(root.left))
            maxRight = max(0, getMaxRecursive(root.right))

            maxDoSplit = root.val + maxLeft + maxRight
            res = max(res, maxDoSplit)

            # fig out max sum if we don't split on root
            # this is what we return (the parents use this
            # for when they DO split, so thus these guys, who
            # are the children, can't split)
            maxNoSplit = max(root.val + maxLeft, root.val + maxRight)
            res = max(res, maxNoSplit)
            return maxNoSplit
        
        getMaxRecursive(root)

        return int(res)
