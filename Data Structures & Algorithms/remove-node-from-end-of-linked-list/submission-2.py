# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        index = 0
        while (index != n):
            first = first.next
            index += 1
        
        # edge case: if n = size then first is already null
        # just remove first element
        if not first:
            return head.next

        second = head
        while (first.next):
            first = first.next
            second = second.next
        
        # now second is right behind the node to delete
        second.next = second.next.next

        return head