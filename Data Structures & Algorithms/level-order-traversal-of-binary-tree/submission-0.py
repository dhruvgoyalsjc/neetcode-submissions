# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        currLvl = []
        res = []

        q.append(root)
        
        while q:
            currLvl.append(q.popleft())
            
            if not q:
                # currLvl complete
                res.append([x.val for x in currLvl])
                for node in currLvl:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                currLvl = [] # reset curr lvl
        
        return res
