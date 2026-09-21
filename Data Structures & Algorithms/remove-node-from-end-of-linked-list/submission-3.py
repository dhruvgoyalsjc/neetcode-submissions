# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        first, second = head, dummy

        for i in range(n): # move first to right n times
            first = first.next
        
        while (first):
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next