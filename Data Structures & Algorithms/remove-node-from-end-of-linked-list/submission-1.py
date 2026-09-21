# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass approach
        # first get overall size of list
        curr = head
        index = 0
        while (curr):
            curr = curr.next
            index += 1
        size = index
        
        # edge case
        if size == n:
            return head.next
        
        curr = head
        index = 0
        while (curr):
            # extra -1 bc we want to be right BEFORE the node to delete
            if index == size - n - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            index += 1
        
        return head
