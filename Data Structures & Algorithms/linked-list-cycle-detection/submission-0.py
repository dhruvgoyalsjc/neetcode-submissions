# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        dummy = ListNode()
        dummy.next = head

        slow, fast = head, None
        if head.next:
            fast = head.next
        else:
            return False

        while (slow != fast):
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True
