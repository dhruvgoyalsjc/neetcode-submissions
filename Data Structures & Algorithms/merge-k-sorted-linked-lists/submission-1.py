# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        dummy = curr = ListNode(None)
        
        while (list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        skip = 1 # how many lists to skip each time we go through the list

        while (skip < len(lists)):
            for i in range(0, len(lists), 2 * skip):
                if (i + skip < len(lists)):
                    lists[i] = self.mergeTwoLists(lists[i], lists[i + skip])
            skip *= 2
        
        return lists[0]
