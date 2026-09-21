# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderIndices = {val: id for id, val in enumerate(inorder)}

        self.rootIndex = 0

        def constructRecursive(l , r):
            if l > r:
                return None
            
            rootVal = preorder[self.rootIndex]
            self.rootIndex += 1

            root = TreeNode(rootVal)
            mid = inOrderIndices[rootVal]

            root.left = constructRecursive(l, mid - 1)
            root.right = constructRecursive(mid+1, r)

            return root
        
        return constructRecursive(0, len(preorder) - 1)
        
            