# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # now curr is None, need to roll back to most recently added
            # node in the stack

            curr = stack.pop()
            cnt += 1
            if (cnt == k):
                return curr.val

            # if we are here, then curr was not what we wanted
            # let's see if there's anything bigger than curr but smaller
            # than curr's parent: go right then left as much as u can
            curr = curr.right
            # now continuing in the while loop will help us find the
            # leftmost guy to add

            