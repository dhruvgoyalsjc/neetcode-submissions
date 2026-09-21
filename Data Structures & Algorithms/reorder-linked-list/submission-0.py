# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # head of second half of list is now at slow.next
        sHead = slow.next
        # break link between halves
        slow.next = None

        # now reverse list from sHead onwards
        prev = None
        curr = sHead
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        sHead = prev # reset slow to be head of new reversed half

        while (head and sHead):
            temp1 = head.next
            head.next = sHead
            temp2 = sHead.next
            sHead.next = temp1
            head = temp1
            sHead = temp2
