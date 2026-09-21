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
        second = slow.next
        # break link between halves and reverse list from second onwards
        prev = slow.next = None
        curr = second
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev # reset second to be head of new reversed half

        while (second):
            temp1 = head.next
            head.next = second
            temp2 = second.next
            second.next = temp1
            head = temp1
            second = temp2
